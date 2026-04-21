"""
Generate time-aligned time-series figures for manuscript revision (Reviewer C14).

Reviewer comment: "Move the blue curve in Figure 6 to the left to align with the other
two curves. In this way, the three curves have the same triggering time. The same
comment for figure 10 and figure 13."

Fix: plot t_rel = t - t_onset on x-axis so shaking onset = 0 for all cases.

Produces:
  aligned_freefield_ru.png   – r_u time histories, free-field at 25 mm depth
  aligned_toe_ru.png         – r_u time histories, embankment toe at 25 mm depth
  aligned_embankment_ru.png  – r_u time histories, beneath embankment crest at 25 mm depth
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

# ── constants ──────────────────────────────────────────────────────────────
ONSET = {'CASE3': 11.74, 'CASE4': 14.18, 'CASE7': 15.46}

# σ'v0 [kPa] from Table in manuscript (depth 25 mm, free-field / toe / embankment)
SIGMA_FF  = 1.4   # free-field, 25 mm depth
SIGMA_TOE = 1.4   # toe,         25 mm depth
SIGMA_EMB = 4.1   # under embankment crest, 25 mm depth (higher due to embankment weight)

# PW sensors at 25 mm depth for each location and case
PW_FREEFIELD  = {'CASE3': 'PW3',    'CASE4': 'PW3',    'CASE7': 'PW8706'}
PW_TOE        = {'CASE3': 'PW6027', 'CASE4': 'PW6027', 'CASE7': 'PW7561'}
PW_EMBANKMENT = {'CASE3': 'PW83-2', 'CASE4': 'PW83-2', 'CASE7': 'PW91'}

STYLES = {
    'CASE3': {'color': '#d62728', 'ls': '-',  'lw': 1.6, 'label': 'Case 3  (3D straight)'},
    'CASE4': {'color': '#2ca02c', 'ls': ':',  'lw': 2.0, 'label': 'Case 4  (3D L-shaped)'},
    'CASE7': {'color': '#1f77b4', 'ls': '--', 'lw': 1.6, 'label': 'Case 7  (2D plane-strain)'},
}

STAGE_BOUNDS = [-1.0, 0.2, 1.2, 3.2, 7.2]   # relative to onset [s]
STAGE_LABELS = ['Stage 1', 'Stage 2', 'Stage 3', 'Stage 4']

# ── data loaders ───────────────────────────────────────────────────────────

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

# ── window: 1 s before onset to 8 s after ─────────────────────────────────

def get_window(df, case, pre=1.0, dur=9.0):
    t0 = ONSET[case] - pre
    t1 = t0 + dur
    dw = df[(df['time'] >= t0) & (df['time'] <= t1)].copy().reset_index(drop=True)
    dw['t_rel'] = dw['time'] - ONSET[case]
    return dw

# ── compute r_u ────────────────────────────────────────────────────────────

def compute_ru(dw, pw_col, sigma_v0):
    """Returns t_rel and r_u arrays for one sensor. u0 = mean of first 0.5 s."""
    if pw_col not in dw.columns:
        return None, None
    raw = dw[pw_col].values.astype(float)
    # baseline: mean of the pre-shaking window (t_rel < 0)
    mask_pre = dw['t_rel'].values < 0.0
    u0 = np.nanmean(raw[mask_pre]) if mask_pre.sum() > 0 else raw[0]
    delta_u = raw - u0
    ru = delta_u / sigma_v0
    return dw['t_rel'].values, ru

# ── figure helper ──────────────────────────────────────────────────────────

def make_ru_figure(pw_map, sigma_v0, title, fname, ru_lim=(-1.5, 3.0)):
    """Single-panel r_u vs t_rel with stage markers and legend."""
    fig, ax = plt.subplots(figsize=(8, 4.5))

    for case, loader in LOADERS.items():
        df = loader()
        dw = get_window(df, case)
        t, ru = compute_ru(dw, pw_map[case], sigma_v0)
        if ru is None:
            print(f"  WARNING: {pw_map[case]} not found in {case}")
            continue
        s = STYLES[case]
        ax.plot(t, ru, color=s['color'], ls=s['ls'], lw=s['lw'],
                label=s['label'], alpha=0.85)

    # liquefaction threshold
    ax.axhline(1.0, color='k', lw=1.0, ls='--', alpha=0.6, label=r'$r_u = 1.0$ (liquefaction)')
    ax.axhline(0.0, color='k', lw=0.5)
    ax.axvline(0.0, color='gray', lw=0.8, ls=':', alpha=0.7)

    # stage boundaries
    for xb in STAGE_BOUNDS:
        ax.axvline(xb, color='steelblue', lw=0.7, ls='--', alpha=0.5)
    ypos = ru_lim[0] + 0.05 * (ru_lim[1] - ru_lim[0])
    for i, lbl in enumerate(STAGE_LABELS):
        xmid = 0.5 * (STAGE_BOUNDS[i] + STAGE_BOUNDS[i+1])
        ax.text(xmid, ypos, lbl, ha='center', va='bottom', fontsize=7.5,
                color='steelblue')

    ax.set_xlabel('Time relative to shaking onset  (s)', fontsize=11)
    ax.set_ylabel(r'$r_u = \Delta u\,/\,\sigma^{\prime}_{v0}$  (–)',
                  fontsize=10)
    ax.set_title(title, fontsize=11, pad=5)
    ax.set_xlim(STAGE_BOUNDS[0] - 0.2, STAGE_BOUNDS[-1] + 0.2)
    ax.set_ylim(*ru_lim)
    ax.xaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
    ax.grid(True, alpha=0.2, linestyle=':')
    ax.legend(fontsize=9, loc='upper left')

    fig.tight_layout()
    path = os.path.join(OUT_DIR, fname)
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}")
    return path

# ── combined 3-panel figure (all locations, side by side) ─────────────────

def make_combined_figure(all_data):
    """3-panel figure: free-field | toe | under-embankment, all time-aligned."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5), constrained_layout=True)
    fig.suptitle(
        r'Time-aligned excess pore water pressure ratio  $r_u$  '
        '(t = 0 = shaking onset)\n'
        'Free-field (25 mm)  |  Embankment toe (25 mm)  |  '
        'Beneath embankment crest (25 mm)',
        fontsize=11)

    configs = [
        (axes[0], PW_FREEFIELD,  SIGMA_FF,
         'Free-field  (25 mm depth)', (-1.0, 2.5)),
        (axes[1], PW_TOE,        SIGMA_TOE,
         'Embankment toe  (25 mm depth)', (-2.0, 3.5)),
        (axes[2], PW_EMBANKMENT, SIGMA_EMB,
         'Beneath embankment crest  (25 mm depth)', (-0.5, 2.0)),
    ]

    for ax, pw_map, sigma, title, ru_lim in configs:
        for case, (t, ru) in all_data.items():
            pw = pw_map[case]
            s = STYLES[case]
            df = LOADERS[case]()
            dw = get_window(df, case)
            t_rel, ru_val = compute_ru(dw, pw, sigma)
            if ru_val is None:
                continue
            ax.plot(t_rel, ru_val, color=s['color'], ls=s['ls'], lw=s['lw'],
                    label=s['label'], alpha=0.85)

        ax.axhline(1.0, color='k', lw=1.0, ls='--', alpha=0.6)
        ax.axhline(0.0, color='k', lw=0.5)
        ax.axvline(0.0, color='gray', lw=0.8, ls=':', alpha=0.7)
        for xb in STAGE_BOUNDS:
            ax.axvline(xb, color='steelblue', lw=0.6, ls='--', alpha=0.4)
        ax.set_xlabel('Time relative to shaking onset (s)', fontsize=10)
        ax.set_ylabel(r'$r_u$', fontsize=11)
        ax.set_title(title, fontsize=10)
        ax.set_xlim(STAGE_BOUNDS[0]-0.2, STAGE_BOUNDS[-1]+0.2)
        ax.set_ylim(*ru_lim)
        ax.grid(True, alpha=0.2, linestyle=':')
        ax.legend(fontsize=8)

    path = os.path.join(OUT_DIR, 'aligned_ru_combined.pdf')
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    print(f"  Saved: {path}")

# ── main ───────────────────────────────────────────────────────────────────

def run():
    print("Generating time-aligned r_u figures (Reviewer C14) …")

    make_ru_figure(
        PW_FREEFIELD, SIGMA_FF,
        r'Free-field $r_u$ time histories  —  25 mm depth'
        '\n(t = 0 = shaking onset; PW3 for Case-A/B, PW8706 for Case-C)',
        'aligned_freefield_ru.pdf',
        ru_lim=(-1.0, 2.5),
    )

    make_ru_figure(
        PW_TOE, SIGMA_TOE,
        r'Embankment toe $r_u$ time histories  —  25 mm depth'
        '\n(t = 0 = shaking onset; PW6027 for Case-A/B, PW7561 for Case-C)',
        'aligned_toe_ru.pdf',
        ru_lim=(-2.0, 3.5),
    )

    make_ru_figure(
        PW_EMBANKMENT, SIGMA_EMB,
        r'Beneath embankment crest $r_u$ time histories  —  25 mm depth'
        '\n(t = 0 = shaking onset; PW83-2 for Case-A/B, PW91 for Case-C)',
        'aligned_embankment_ru.pdf',
        ru_lim=(-0.5, 2.0),
    )

    # dummy container for combined figure (data loaded inside)
    make_combined_figure({'CASE3': (None, None), 'CASE4': (None, None), 'CASE7': (None, None)})

    print("Done.")


if __name__ == '__main__':
    run()
