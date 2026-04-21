"""
Verification of shear stress (tau) and shear strain (gamma) calculation.

Method: Koga (1990) / Watanabe (2023) shear-beam approach.

Coordinate convention
---------------------
z = height measured from container BASE (z = 0).
  z = 0.000 m : container base (shaking table)
  z = 0.200 m : ground surface (top of liquefiable foundation layer)
  z = 0.400 m : top of embankment

Equations
---------
Shear strain between sensors at z_lower and z_upper (z_upper > z_lower):
    gamma(t) = [d(z_upper, t) - d(z_lower, t)] / dz    (dimensionless)

    where d is baseline-corrected horizontal displacement from double
    integration of band-pass-filtered acceleration.
    CRITICAL: convert G -> m/s² BEFORE integrating.

Shear stress at elevation z_k (evaluated at the lower sensor):
    tau(z_k, t) = sum_{i: z_i > z_k} rho_i * h_i * a(z_i, t)   (Pa -> kPa)

    h_i = layer thickness assigned to sensor i via midpoint rule,
          using z_k as the lower boundary for the first (lowest) sensor.

Known issue in original generate_figures.py
-------------------------------------------
Both gamma and tau were computed WITHOUT multiplying acceleration by 9.81
before integration / summation. Because the same factor is missing from
both axes, the loop SHAPE is preserved but all axis values are too small
by a factor of 9.81.

  tau_correct  = tau_original  × 9.81
  gamma_correct = gamma_original × 9.81    (same factor, via displacement)

This script produces CORRECT values.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt
from scipy.integrate import cumulative_trapezoid
import os, warnings
warnings.filterwarnings('ignore')

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE    = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE, 'actual_test_data')
OUT_DIR  = os.path.dirname(os.path.abspath(__file__))

# ─── Physical constants ───────────────────────────────────────────────────────
G_TO_MS2  = 9.81      # 1 G = 9.81 m/s²
RHO_SAT   = 1900.0    # kg/m³  (Silica Sand No.7, Dr≈52%, saturated)
Z_SURFACE = 0.200     # m  ground surface from container base
Z_EMB_TOP = 0.400     # m  embankment top from container base
FS        = 200.0     # Hz  (dt = 5 ms)

# ─── Sensor heights from container base [m] ───────────────────────────────────
#  (from sensor_coordinates.json; same layout for CASE3, CASE4, CASE7)
SENSOR_Z = {
    'AC70-2': 0.000,   # container base / shaking table (reference)
    'AC31'  : 0.075,   # under embankment, 125 mm below surface
    'AC24'  : 0.025,   # at toe, 175 mm below surface
    'AC25'  : 0.125,   # at toe,  75 mm below surface
    'AC72-2': 0.175,   # under embankment,  25 mm below surface
    'AC82'  : 0.175,   # CASE7 equivalent of AC72-2
    'AC11'  : 0.275,   # in embankment,     75 mm above surface
    'AC26'  : 0.375,   # in embankment,    175 mm above surface
    'AC75'  : 0.075,   # CASE7 toe (assumed same elevation as AC31)
}

# ─── Shaking onset times from AC70-2 > 0.05 G ───────────────────────────────
ONSET = {'CASE3': 11.74, 'CASE4': 14.18, 'CASE7': 15.46}

# ─── Signal processing ────────────────────────────────────────────────────────

def bandpass(x, lo=1.0, hi=30.0, fs=FS, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [lo/nyq, hi/nyq], btype='band')
    return filtfilt(b, a, x)

def highpass(x, cutoff=0.1, fs=FS, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, cutoff/nyq, btype='high')
    return filtfilt(b, a, x)

def acc_to_disp_m(acc_g, t):
    """
    Convert filtered acceleration [G] to baseline-corrected displacement [m].
    Applies G -> m/s² conversion BEFORE integration.
    """
    a_ms2 = bandpass(acc_g) * G_TO_MS2             # G  -> m/s²
    vel   = cumulative_trapezoid(a_ms2, t, initial=0.0)   # m/s
    disp  = cumulative_trapezoid(vel,   t, initial=0.0)   # m
    return highpass(disp)                            # m  (drift removed)

# ─── Data loaders ─────────────────────────────────────────────────────────────

def load_case7(path):
    df = pd.read_csv(path, skiprows=3)
    df = df[~df['Name'].isin(['Unit','Maximum','Minimum','Average'])].copy()
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df.rename(columns={'Measurement time':'time'}).dropna(subset=['time'])

def load_excel(path):
    df = pd.read_excel(path, header=3)
    df = df[~df['Name'].isin(['Unit','Maximum','Minimum','Average'])].copy()
    df = df.rename(columns={'Measurement time':'time'})
    for c in df.columns[1:]:
        df[c] = pd.to_numeric(df[c], errors='coerce')
    return df.dropna(subset=['time'])

def window(df, onset, pre=1.0, dur=9.0):
    return df[(df['time'] >= onset-pre) & (df['time'] <= onset-pre+dur)].copy().reset_index(drop=True)

# ─── Layer-height assignment (midpoint rule) ──────────────────────────────────

def layer_heights(sensors_above_zk, z_k, z_top=Z_EMB_TOP):
    """
    Compute representative layer thickness for each sensor above z_k.

    sensors_above_zk : list of (name, z) sorted from LOWEST to HIGHEST z,
                       all with z > z_k.
    z_k              : elevation of evaluation point (lower sensor) [m]
    z_top            : elevation of model top [m]

    Midpoint rule:
      lower boundary of sensor i = midpoint(z_{i-1}, z_i)   (or midpoint(z_k, z_i) for i=0)
      upper boundary of sensor i = midpoint(z_i, z_{i+1})   (or midpoint(z_i, z_top) for last)
    """
    n = len(sensors_above_zk)
    h = {}
    for i, (name, z) in enumerate(sensors_above_zk):
        z_prev = z_k if i == 0 else sensors_above_zk[i-1][1]
        z_next = z_top if i == n-1 else sensors_above_zk[i+1][1]
        lower_mid = (z_prev + z) / 2.0
        upper_mid = (z      + z_next) / 2.0
        h[name] = upper_mid - lower_mid
    return h

# ─── Core tau-gamma computation ───────────────────────────────────────────────

def tau_gamma(df, acc_lower, acc_upper, sensors_above_zk, z_k, z_top=Z_EMB_TOP):
    """
    Compute shear stress and shear strain time series for one sensor pair.

    Parameters
    ----------
    df               : windowed DataFrame
    acc_lower        : name of lower (deeper) accelerometer (at z_k)
    acc_upper        : name of upper (shallower) accelerometer
    sensors_above_zk : list of (name, z) sorted LOW -> HIGH, z > z_k
    z_k              : elevation of lower sensor [m]
    z_top            : model top elevation [m]

    Returns
    -------
    t        : time array (s)
    gamma_pct: shear strain [%]
    tau_kpa  : shear stress [kPa]
    """
    t = df['time'].values

    if acc_lower not in df.columns or acc_upper not in df.columns:
        return t, None, None

    # ── gamma ────────────────────────────────────────────────────────────
    d_lo = acc_to_disp_m(df[acc_lower].values.astype(float), t)
    d_hi = acc_to_disp_m(df[acc_upper].values.astype(float), t)
    dz   = abs(SENSOR_Z[acc_upper] - SENSOR_Z[acc_lower])
    gamma_pct = (d_hi - d_lo) / dz * 100.0     # %

    # ── tau ──────────────────────────────────────────────────────────────
    h = layer_heights(sensors_above_zk, z_k, z_top)
    tau_pa = np.zeros(len(t))
    for name, _ in sensors_above_zk:
        if name in df.columns:
            a_ms2   = bandpass(df[name].values.astype(float)) * G_TO_MS2
            tau_pa += RHO_SAT * h[name] * a_ms2
    tau_kpa = tau_pa / 1000.0

    return t, gamma_pct, tau_kpa

# ─── Load data ────────────────────────────────────────────────────────────────

def load_all():
    return {
        'CASE3': load_excel(os.path.join(DATA_DIR, 'CASE3.xls')),
        'CASE4': load_excel(os.path.join(DATA_DIR, 'CASE4.xls')),
        'CASE7': load_case7(os.path.join(DATA_DIR, 'CASE7.CSV')),
    }

# ─── Main ─────────────────────────────────────────────────────────────────────

def run():
    print("=" * 65)
    print("TAU-GAMMA VERIFICATION  (corrected G -> m/s² conversion)")
    print("=" * 65)

    datasets = load_all()

    # Sensor pairs and column definitions
    # --- Under embankment crest ---
    # Lower: AC31 (z=0.075), Upper: AC72-2 or AC82 (z=0.175)
    # Sensors above AC31: [AC72-2/AC82, AC11, AC26]
    # --- At embankment toe ---
    # Lower: AC24 (z=0.025), Upper: AC25 (z=0.125)
    # Sensors above AC24 at TOE: [AC25] only (no embankment above toe)
    # z_top for toe = Z_SURFACE (no embankment contribution at toe location)

    fig, axes = plt.subplots(2, 3, figsize=(16, 10),
                             constrained_layout=True)
    fig.suptitle(
        "τ–γ Loop Verification  (corrected: G→m/s² before integration)\n"
        "Sensor layout: AC31↔AC72-2 (under crest)  |  AC24↔AC25 (toe)",
        fontsize=12)

    styles = {
        'CASE3': ('red',   '-',  'Case-A (3D straight)'),
        'CASE4': ('green', ':',  'Case-B (3D L-shaped)'),
        'CASE7': ('blue',  '--', 'Case-C (2D plane-strain)'),
    }

    summary = {}

    for col, (case, df) in enumerate(datasets.items()):
        onset = ONSET[case]
        dw = window(df, onset)
        t_abs = dw['time'].values
        t_rel = t_abs - onset          # aligned: 0 = shaking onset

        colour, ls, label = styles[case]

        # ── Under embankment crest ────────────────────────────────────
        upper_emb = 'AC82' if (case == 'CASE7' and 'AC82' in dw.columns) else 'AC72-2'
        sensors_emb = [(upper_emb, SENSOR_Z[upper_emb]),
                       ('AC11',    SENSOR_Z['AC11']),
                       ('AC26',    SENSOR_Z['AC26'])]
        sensors_emb = [(n, z) for n, z in sensors_emb if n in dw.columns]

        _, g_emb, t_emb = tau_gamma(dw, 'AC31', upper_emb,
                                    sensors_emb, SENSOR_Z['AC31'], Z_EMB_TOP)

        # ── At toe ───────────────────────────────────────────────────
        sensors_toe = [('AC25', SENSOR_Z['AC25'])]
        _, g_toe, t_toe = tau_gamma(dw, 'AC24', 'AC25',
                                    sensors_toe, SENSOR_Z['AC24'], Z_SURFACE)

        summary[case] = {
            'g_emb_pct_range': (g_emb.min(), g_emb.max()) if g_emb is not None else None,
            't_emb_kpa_range': (t_emb.min(), t_emb.max()) if t_emb is not None else None,
            'g_toe_pct_range': (g_toe.min(), g_toe.max()) if g_toe is not None else None,
            't_toe_kpa_range': (t_toe.min(), t_toe.max()) if t_toe is not None else None,
        }

        # ── Loop plots ────────────────────────────────────────────────
        ax = axes[0, col]
        if g_emb is not None:
            ax.plot(g_emb, t_emb, color=colour, lw=1.0, alpha=0.8)
        ax.set_title(f"{label}\nUnder embankment crest\n(AC31 ↔ {upper_emb})")
        ax.set_xlabel("γ  (%)")
        ax.set_ylabel("τ  (kPa)")
        ax.axhline(0, color='k', lw=0.5)
        ax.axvline(0, color='k', lw=0.5)
        ax.grid(True, alpha=0.3)

        ax = axes[1, col]
        if g_toe is not None:
            ax.plot(g_toe, t_toe, color=colour, lw=1.0, alpha=0.8)
        ax.set_title(f"{label}\nAt embankment toe\n(AC24 ↔ AC25)")
        ax.set_xlabel("γ  (%)")
        ax.set_ylabel("τ  (kPa)")
        ax.axhline(0, color='k', lw=0.5)
        ax.axvline(0, color='k', lw=0.5)
        ax.grid(True, alpha=0.3)

    # ── Print summary ─────────────────────────────────────────────────
    print(f"\n{'Case':<8} {'Location':<22} {'γ range (%)':<24} {'τ range (kPa)'}")
    print("-" * 70)
    for case, res in summary.items():
        if res['g_emb_pct_range']:
            g = res['g_emb_pct_range']
            t = res['t_emb_kpa_range']
            print(f"{case:<8} {'under embankment':<22} "
                  f"[{g[0]:+.2f} .. {g[1]:+.2f}]   "
                  f"[{t[0]:+.2f} .. {t[1]:+.2f}]")
        if res['g_toe_pct_range']:
            g = res['g_toe_pct_range']
            t = res['t_toe_kpa_range']
            print(f"{case:<8} {'at toe':<22} "
                  f"[{g[0]:+.2f} .. {g[1]:+.2f}]   "
                  f"[{t[0]:+.2f} .. {t[1]:+.2f}]")

    print()
    print("Reference (original manuscript, estimated from figures):")
    print("  Under crest:   γ ≈ ±0.6%  (CASE7),  ±2.2%  (CASE3),  ±3.4%  (CASE4)")
    print("  At toe:        γ ≈ ±0.5%  (CASE7),  ±0.8%  (CASE3),  ±1.7%  (CASE4)")
    print("  τ peak:        ≈ ±7-8 kPa (CASE7),  ±5-6 kPa (CASE3), ±4-5 kPa (CASE4)")
    print()
    print("Note: original manuscript values were produced WITHOUT the G->m/s² conversion.")
    print("      Correct values are ~9.81× larger on both axes (loop shape unchanged).")

    out_path = os.path.join(OUT_DIR, 'verify_tau_gamma.png')
    plt.savefig(out_path, dpi=150, bbox_inches='tight')
    print(f"\nLoop plot saved -> {out_path}")
    plt.close()

    return summary


if __name__ == '__main__':
    run()
