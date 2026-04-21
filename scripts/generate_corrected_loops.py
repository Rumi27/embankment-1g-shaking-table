"""
Generate corrected tau-gamma (τ–γ) loop figures for manuscript revision.

Fix applied: acceleration converted G -> m/s² BEFORE double integration
so that displacement and shear strain are in correct physical units.

Produces three publication-quality figures:
  1. loops_under_embankment.png  – τ–γ beneath embankment crest
  2. loops_at_toe.png            – τ–γ at embankment toe
  3. loops_combined.png          – 2×3 panel comparison

Sensor layout (height from container base, z=0):
  z = 0.000 m  container base
  z = 0.075 m  AC31   foundation deep     (125 mm below surface)
  z = 0.125 m  AC25   toe shallow         ( 75 mm below surface)
  z = 0.025 m  AC24   toe deep            (175 mm below surface)
  z = 0.175 m  AC72-2 / AC82  foundation top (25 mm below surface)
  z = 0.200 m  ---- ground surface ----
  z = 0.275 m  AC11   embankment lower    ( 75 mm above surface)
  z = 0.375 m  AC26   embankment upper    (175 mm above surface)
  z = 0.400 m  embankment top
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from scipy.signal import butter, filtfilt
from scipy.integrate import cumulative_trapezoid
import os, warnings
warnings.filterwarnings('ignore')

# ── paths ──────────────────────────────────────────────────────────────────
BASE     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, 'actual_test_data')
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

# ── constants ──────────────────────────────────────────────────────────────
G2MS2    = 9.81
RHO      = 1900.0      # kg/m³  saturated density
Z_SURF   = 0.200       # m  ground surface from base
Z_TOP    = 0.400       # m  embankment top from base
FS       = 200.0       # Hz

SENSOR_Z = {
    'AC70-2': 0.000, 'AC31': 0.075, 'AC24': 0.025, 'AC25': 0.125,
    'AC72-2': 0.175, 'AC82': 0.175,
    'AC11'  : 0.275, 'AC26': 0.375,
    'AC75'  : 0.075,
}

# shaking onset (s) and display offset for time-alignment
ONSET   = {'CASE3': 11.74, 'CASE4': 14.18, 'CASE7': 15.46}

# ── signal processing ──────────────────────────────────────────────────────

def bp(x, lo=1.0, hi=30.0, fs=FS, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lo/nyq, hi/nyq], btype='band')
    return filtfilt(b, a, x)

def hp(x, cutoff=0.1, fs=FS, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, cutoff/nyq, btype='high')
    return filtfilt(b, a, x)

def acc_to_disp(acc_g, t):
    """G -> m/s² -> velocity -> displacement (m), drift removed."""
    a_ms2 = bp(acc_g) * G2MS2
    vel   = cumulative_trapezoid(a_ms2, t, initial=0.0)
    disp  = cumulative_trapezoid(vel,   t, initial=0.0)
    return hp(disp)

# ── data loaders ───────────────────────────────────────────────────────────

def load_csv(path):
    df = pd.read_csv(path, skiprows=3)
    df = df[~df['Name'].isin(['Unit','Maximum','Minimum','Average'])].copy()
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df.rename(columns={'Measurement time': 'time'}).dropna(subset=['time'])

def load_xls(path):
    df = pd.read_excel(path, header=3)
    df = df[~df['Name'].isin(['Unit','Maximum','Minimum','Average'])].copy()
    df = df.rename(columns={'Measurement time': 'time'})
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df.dropna(subset=['time'])

def get_window(df, case, pre=1.0, dur=9.0):
    t0 = ONSET[case] - pre
    t1 = t0 + dur
    dw = df[(df['time'] >= t0) & (df['time'] <= t1)].copy().reset_index(drop=True)
    dw['t_rel'] = dw['time'] - ONSET[case]   # 0 = shaking onset
    return dw

# ── layer heights (midpoint rule) ──────────────────────────────────────────

def layer_h(sensors_above, z_k, z_top_col):
    """
    sensors_above : [(name, z), ...] sorted LOW -> HIGH, all z > z_k
    Returns dict  name -> layer thickness [m]
    """
    n  = len(sensors_above)
    h  = {}
    for i, (name, z) in enumerate(sensors_above):
        z_prev = z_k if i == 0 else sensors_above[i-1][1]
        z_next = z_top_col if i == n-1 else sensors_above[i+1][1]
        h[name] = (z + z_next)/2.0 - (z_prev + z)/2.0
    return h

# ── core tau-gamma ─────────────────────────────────────────────────────────

def compute(dw, lower, upper, col_sensors, z_k, z_top_col):
    """
    lower        : sensor name at z_k (deeper)
    upper        : sensor name above z_k (shallower)
    col_sensors  : [(name, z), ...] ALL sensors above z_k, sorted LOW -> HIGH
    Returns gamma_pct, tau_kpa  (arrays aligned with dw['t_rel'])
    """
    t = dw['time'].values
    if lower not in dw.columns or upper not in dw.columns:
        return None, None

    d_lo = acc_to_disp(dw[lower].values.astype(float), t)
    d_hi = acc_to_disp(dw[upper].values.astype(float), t)
    dz   = abs(SENSOR_Z[upper] - SENSOR_Z[lower])
    gamma_pct = (d_hi - d_lo) / dz * 100.0

    h = layer_h([(n, z) for n, z in col_sensors if n in dw.columns], z_k, z_top_col)
    tau_pa = np.zeros(len(t))
    for name, _ in col_sensors:
        if name in dw.columns:
            tau_pa += RHO * h.get(name, 0.0) * bp(dw[name].values.astype(float)) * G2MS2
    tau_kpa = tau_pa / 1000.0

    return gamma_pct, tau_kpa

# ── load all data ──────────────────────────────────────────────────────────

LOADERS = {
    'CASE3': lambda: load_xls(os.path.join(DATA_DIR, 'CASE3.xls')),
    'CASE4': lambda: load_xls(os.path.join(DATA_DIR, 'CASE4.xls')),
    'CASE7': lambda: load_csv(os.path.join(DATA_DIR, 'CASE7.CSV')),
}

STYLES = {
    'CASE3': {'color': '#d62728', 'ls': '-',  'lw': 1.8, 'label': 'Case 3  (3D straight)'},
    'CASE4': {'color': '#2ca02c', 'ls': ':',  'lw': 2.2, 'label': 'Case 4  (3D L-shaped)'},
    'CASE7': {'color': '#1f77b4', 'ls': '--', 'lw': 1.8, 'label': 'Case 7  (2D plane-strain)'},
}

# ── figure helpers ─────────────────────────────────────────────────────────

def style_ax(ax, xlabel=r'$\gamma$ (%)', ylabel=r'$\tau$ (kPa)', title=''):
    ax.set_xlabel(xlabel, fontsize=11)
    ax.set_ylabel(ylabel, fontsize=11)
    ax.set_title(title, fontsize=11, pad=4)
    ax.axhline(0, color='k', lw=0.6)
    ax.axvline(0, color='k', lw=0.6)
    ax.grid(True, alpha=0.25, linestyle=':')
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

def add_peak_text(ax, gmax, tmax):
    ax.text(0.97, 0.97,
            f'$\\gamma_{{\\max}}$ = {gmax:.1f}%\n$\\tau_{{\\max}}$ = {tmax:.1f} kPa',
            transform=ax.transAxes, ha='right', va='top',
            fontsize=8, bbox=dict(boxstyle='round,pad=0.3', fc='white', alpha=0.7))

# ── main ───────────────────────────────────────────────────────────────────

def run():
    print("Generating corrected τ–γ loop figures …")

    # collect results
    emb = {}   # under embankment
    toe = {}   # at toe

    for case, loader in LOADERS.items():
        df  = loader()
        dw  = get_window(df, case)
        upper_emb = 'AC82' if (case == 'CASE7' and 'AC82' in dw.columns) else 'AC72-2'

        # under embankment: lower=AC31(z=0.075), upper=AC72-2/AC82(z=0.175)
        col_emb = [(upper_emb,    SENSOR_Z[upper_emb]),
                   ('AC11',       SENSOR_Z['AC11']),
                   ('AC26',       SENSOR_Z['AC26'])]
        col_emb = [(n, z) for n, z in col_emb if n in dw.columns]
        g_emb, t_emb = compute(dw, 'AC31', upper_emb, col_emb,
                                SENSOR_Z['AC31'], Z_TOP)

        # at toe: lower=AC24(z=0.025), upper=AC25(z=0.125)
        # no embankment above toe → z_top = Z_SURF
        col_toe = [('AC25', SENSOR_Z['AC25'])]
        g_toe, t_toe = compute(dw, 'AC24', 'AC25', col_toe,
                               SENSOR_Z['AC24'], Z_SURF)

        emb[case] = (g_emb, t_emb)
        toe[case] = (g_toe, t_toe)

        # diagnostics
        if g_emb is not None:
            print(f"  {case} under embankment: "
                  f"γ=[{g_emb.min():+.2f}..{g_emb.max():+.2f}]%  "
                  f"τ=[{t_emb.min():+.2f}..{t_emb.max():+.2f}] kPa")
        if g_toe is not None:
            print(f"  {case} at toe:           "
                  f"γ=[{g_toe.min():+.2f}..{g_toe.max():+.2f}]%  "
                  f"τ=[{t_toe.min():+.2f}..{t_toe.max():+.2f}] kPa")

    # ── Figure 1: under embankment (single panel, all 3 cases) ────────────
    fig1, ax1 = plt.subplots(figsize=(7, 5))
    for case, (g, t) in emb.items():
        if g is None:
            continue
        s = STYLES[case]
        ax1.plot(g, t, color=s['color'], ls=s['ls'], lw=s['lw'],
                 label=s['label'], alpha=0.85)
    style_ax(ax1, title='Shear Stress–Strain Loops — Beneath Embankment Crest\n'
             r'(AC31 $\leftrightarrow$ AC72-2/AC82,  $\Delta z$ = 100 mm)')
    ax1.legend(fontsize=9, loc='upper left')
    fig1.tight_layout()
    p1 = os.path.join(OUT_DIR, 'loops_under_embankment.pdf')
    fig1.savefig(p1, bbox_inches='tight')
    plt.close(fig1)
    print(f"\nSaved: {p1}")

    # ── Figure 2: at toe (single panel, all 3 cases) ──────────────────────
    fig2, ax2 = plt.subplots(figsize=(7, 5))
    for case, (g, t) in toe.items():
        if g is None:
            continue
        s = STYLES[case]
        ax2.plot(g, t, color=s['color'], ls=s['ls'], lw=s['lw'],
                 label=s['label'], alpha=0.85)
    style_ax(ax2, title='Shear Stress–Strain Loops — At Embankment Toe\n'
             r'(AC24 $\leftrightarrow$ AC25,  $\Delta z$ = 100 mm,  no embankment surcharge)')
    ax2.legend(fontsize=9, loc='upper left')
    fig2.tight_layout()
    p2 = os.path.join(OUT_DIR, 'loops_at_toe.pdf')
    fig2.savefig(p2, bbox_inches='tight')
    plt.close(fig2)
    print(f"Saved: {p2}")

    # ── Figure 3: 2×3 panel (each case its own column) ────────────────────
    fig3, axes = plt.subplots(2, 3, figsize=(15, 9), constrained_layout=True)
    fig3.suptitle(
        r'Corrected $\tau$–$\gamma$ Loops  (G $\rightarrow$ m/s² before integration)'
        '\nTop row: beneath embankment crest  |  Bottom row: at toe',
        fontsize=12)

    for col, (case, sty) in enumerate(STYLES.items()):
        c, ls, lw, lbl = sty['color'], sty['ls'], sty['lw'], sty['label']

        # top: under embankment
        ax = axes[0, col]
        g_e, t_e = emb[case]
        if g_e is not None:
            ax.plot(g_e, t_e, color=c, ls=ls, lw=lw, alpha=0.85)
            add_peak_text(ax, max(abs(g_e.min()), g_e.max()),
                              max(abs(t_e.min()), t_e.max()))
        style_ax(ax, title=f'{lbl}\nBeneath embankment crest')

        # bottom: at toe
        ax = axes[1, col]
        g_t, t_t = toe[case]
        if g_t is not None:
            ax.plot(g_t, t_t, color=c, ls=ls, lw=lw, alpha=0.85)
            add_peak_text(ax, max(abs(g_t.min()), g_t.max()),
                              max(abs(t_t.min()), t_t.max()))
        style_ax(ax, title=f'{lbl}\nAt embankment toe')

    p3 = os.path.join(OUT_DIR, 'loops_combined.pdf')
    fig3.savefig(p3, bbox_inches='tight')
    plt.close(fig3)
    print(f"Saved: {p3}")
    print("\nDone.")


if __name__ == '__main__':
    run()
