"""
Generate EPWP vs acceleration cross-plots for Reviewer C13.

Reviewer: "There are many spikes in the excess pore pressure curves; these may be due
to boundary effects / reflected P-waves. The authors could also plot the acceleration
response at the same level to check if there are P-wave induced spikes."

This script produces:
  epwp_acc_crossplot.png  –  3-panel figure (one column per case):
    Top   : EPWP at free-field 25mm depth (kPa)
    Bottom: Acceleration at nearest sensor depth (G)
  Time-aligned (t_rel = t - onset).

If EPWP spikes correlate with acceleration spikes → P-wave / kinematic boundary effect.
If they do not correlate → pore pressure measurement artifact or dilatancy.
"""

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import os, warnings
warnings.filterwarnings('ignore')

# ── paths ──────────────────────────────────────────────────────────────────
BASE     = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, 'actual_test_data')
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

ONSET = {'CASE3': 11.74, 'CASE4': 14.18, 'CASE7': 15.46}

# Free-field EPWP sensor at 25 mm depth
PW_FF = {'CASE3': 'PW3', 'CASE4': 'PW3', 'CASE7': 'PW8706'}

# Nearest available accelerometers to the free-field location
# (no free-field accelerometer at 25mm — using base and nearest soil sensor)
ACC_BASE  = 'AC70-2'    # base acceleration (z=0)
ACC_SOIL  = {'CASE3': 'AC31', 'CASE4': 'AC31', 'CASE7': 'AC31'}  # z=0.075 m

STYLES = {
    'CASE3': {'color': '#d62728', 'label': 'Case 3  (3D straight)'},
    'CASE4': {'color': '#2ca02c', 'label': 'Case 4  (3D L-shaped)'},
    'CASE7': {'color': '#1f77b4', 'label': 'Case 7  (2D plane-strain)'},
}

# ── loaders ────────────────────────────────────────────────────────────────

def load_csv(path):
    df = pd.read_csv(path, skiprows=3, low_memory=False)
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

LOADERS = {
    'CASE3': lambda: load_xls(os.path.join(DATA_DIR, 'CASE3.xls')),
    'CASE4': lambda: load_xls(os.path.join(DATA_DIR, 'CASE4.xls')),
    'CASE7': lambda: load_csv(os.path.join(DATA_DIR, 'CASE7.CSV')),
}

def get_window(df, case, pre=1.0, dur=9.0):
    t0 = ONSET[case] - pre
    t1 = t0 + dur
    dw = df[(df['time'] >= t0) & (df['time'] <= t1)].copy().reset_index(drop=True)
    dw['t_rel'] = dw['time'] - ONSET[case]
    return dw

def delta_u(dw, pw_col):
    """Excess pore pressure: subtract pre-shaking mean (t_rel < 0)."""
    if pw_col not in dw.columns:
        return None
    raw = dw[pw_col].values.astype(float)
    mask = dw['t_rel'].values < 0.0
    u0 = np.nanmean(raw[mask]) if mask.sum() > 0 else raw[0]
    return raw - u0

# ── main figure ────────────────────────────────────────────────────────────

def run():
    print("Generating EPWP–acceleration cross-plot (Reviewer C13) …")

    fig, axes = plt.subplots(2, 3, figsize=(15, 8), constrained_layout=True)
    fig.suptitle(
        'Free-field EPWP spikes vs acceleration response (Reviewer C13)\n'
        'Top: excess pore water pressure at 25 mm depth  |  '
        'Bottom: base acceleration + soil acceleration at 75 mm depth\n'
        'Note: no free-field accelerometer at 25 mm — nearest sensor (AC31, z = 75 mm) used',
        fontsize=10)

    for col, case in enumerate(['CASE3', 'CASE4', 'CASE7']):
        df = LOADERS[case]()
        dw = get_window(df, case)
        t  = dw['t_rel'].values
        s  = STYLES[case]

        # ── EPWP panel ────────────────────────────────────────────────
        ax_top = axes[0, col]
        du = delta_u(dw, PW_FF[case])
        if du is not None:
            ax_top.plot(t, du, color=s['color'], lw=0.8, alpha=0.9)
        ax_top.axhline(0, color='k', lw=0.5)
        ax_top.axvline(0, color='gray', lw=0.7, ls=':', alpha=0.6)
        ax_top.set_title(f"{s['label']}\nFree-field EPWP  (PW = {PW_FF[case]})",
                         fontsize=9.5)
        ax_top.set_ylabel(r'$\Delta u$  (kPa)', fontsize=9)
        ax_top.set_xlabel('t – onset  (s)', fontsize=9)
        ax_top.grid(True, alpha=0.2, linestyle=':')
        ax_top.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
        ax_top.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

        # ── acceleration panel ────────────────────────────────────────
        ax_bot = axes[1, col]
        # base
        if ACC_BASE in dw.columns:
            ax_bot.plot(t, dw[ACC_BASE].values.astype(float),
                        color='k', lw=0.7, alpha=0.7, label=f'{ACC_BASE} (base, z=0)')
        # soil
        acc_soil_col = ACC_SOIL[case]
        if acc_soil_col in dw.columns:
            ax_bot.plot(t, dw[acc_soil_col].values.astype(float),
                        color=s['color'], lw=0.8, alpha=0.85,
                        label=f'{acc_soil_col} (z=75 mm, under emb.)')

        ax_bot.axhline(0, color='k', lw=0.5)
        ax_bot.axvline(0, color='gray', lw=0.7, ls=':', alpha=0.6)
        ax_bot.set_title('Acceleration comparison\n'
                         '(base = black; soil at 75 mm = coloured)', fontsize=9.5)
        ax_bot.set_ylabel('Acceleration  (G)', fontsize=9)
        ax_bot.set_xlabel('t – onset  (s)', fontsize=9)
        ax_bot.legend(fontsize=7.5, loc='upper left')
        ax_bot.grid(True, alpha=0.2, linestyle=':')
        ax_bot.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
        ax_bot.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))

        print(f"  {case}: EPWP peak = {du.max() if du is not None else 'N/A':.3f} kPa")

    path = os.path.join(OUT_DIR, 'epwp_acc_crossplot.pdf')
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    print(f"\nSaved: {path}")

    # ── CASE7 detail: zoom on Stage 4 to see spike correlation ────────────
    print("Generating CASE7 detail zoom (Stage 4 spikes) …")
    df7 = LOADERS['CASE7']()
    dw7 = get_window(df7, 'CASE7', pre=1.0, dur=9.0)
    t7  = dw7['t_rel'].values
    du7 = delta_u(dw7, 'PW8706')

    fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6), sharex=True,
                                     constrained_layout=True)
    fig2.suptitle(
        'Case-C (2D plane-strain): EPWP spikes vs. base & soil acceleration — Stage 4 detail\n'
        'Correlation in timing indicates P-wave / boundary-driven pressure fluctuation',
        fontsize=10)

    if du7 is not None:
        ax1.plot(t7, du7, color='#1f77b4', lw=0.9)
    ax1.axhline(0, color='k', lw=0.5)
    ax1.set_ylabel(r'$\Delta u$ free-field  (kPa)', fontsize=10)
    ax1.grid(True, alpha=0.2)
    ax1.set_title('Free-field EPWP  (PW8706, z = 25 mm)', fontsize=10)

    if 'AC70-2' in dw7.columns:
        ax2.plot(t7, dw7['AC70-2'].values.astype(float),
                 color='k', lw=0.7, alpha=0.7, label='AC70-2 (base, z=0)')
    if 'AC31' in dw7.columns:
        ax2.plot(t7, dw7['AC31'].values.astype(float),
                 color='#ff7f0e', lw=0.8, alpha=0.85,
                 label='AC31 (z=75 mm, under emb.)')
    if 'AC24' in dw7.columns:
        ax2.plot(t7, dw7['AC24'].values.astype(float),
                 color='#1f77b4', lw=0.8, alpha=0.85, ls='--',
                 label='AC24 (z=25 mm, at toe)')
    ax2.axhline(0, color='k', lw=0.5)
    ax2.set_ylabel('Acceleration  (G)', fontsize=10)
    ax2.set_xlabel('Time relative to shaking onset  (s)', fontsize=10)
    ax2.legend(fontsize=8.5)
    ax2.grid(True, alpha=0.2)
    ax2.set_title('Accelerometer comparison at/near free-field', fontsize=10)

    ax2.set_xlim(3.0, 8.0)   # zoom to Stage 4 where spikes dominate

    path2 = os.path.join(OUT_DIR, 'epwp_acc_case7_detail.pdf')
    fig2.savefig(path2, bbox_inches='tight')
    plt.close(fig2)
    print(f"Saved: {path2}")
    print("Done.")


if __name__ == '__main__':
    run()
