"""
Recreate Figure 5 (calculation schematic) with corrected equations.

Errors in original Figure6.jpg (Figure 5 in manuscript):
  1. tau_1 used triple integral ∭V  — wrong; correct is single integral ∫ or discrete sum
  2. d_2 was missing the "=" sign
  3. The tau(z_k,t) equation in the figure had no equation number (addressed in LaTeX)

Correct formulas (Koga 1990 / Watanabe 2023 shear-beam method):
  d_i = ∫∫ a_i dt          (double integration of filtered acceleration)
  γ_{i/j}(t) = (d_i - d_j) / Δz_{ij}   (shear strain)
  τ(z_k, t) = Σ_i ρ_i · h_i · a_i(t)   (shear stress, summed above z_k)
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.lines as mlines
import numpy as np
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

def draw_schematic():
    fig, ax = plt.subplots(figsize=(9, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # ── column boundaries ────────────────────────────────────────────────
    col_x0, col_x1 = 1.5, 4.5   # column box x range
    z_surf   = 9.0               # y-coord of ground surface
    z_ac1    = 7.5               # y-coord of AC1 (top sensor)
    z_ac2    = 5.0               # y-coord of AC2 (middle sensor)
    z_ac3    = 2.5               # y-coord of AC3 (bottom sensor)
    z_base   = 1.0               # container base

    # Hatching at surface
    ax.plot([col_x0, col_x1], [z_surf, z_surf], 'k-', lw=2)
    for xi in np.arange(col_x0 + 0.1, col_x1, 0.25):
        ax.plot([xi, xi - 0.15], [z_surf, z_surf + 0.3], 'k-', lw=0.8)

    # Column walls
    ax.plot([col_x0, col_x0], [z_base, z_surf], 'k--', lw=1.2)
    ax.plot([col_x1, col_x1], [z_base, z_surf], 'k--', lw=1.2)

    # Surface label
    ax.text(col_x0 - 0.15, z_surf + 0.15, 'Surface', ha='right', va='bottom',
            fontsize=10, style='italic')

    # ── embankment area trapezoid ─────────────────────────────────────────
    emb_ys = [z_surf, z_surf + 0.6, z_surf + 0.6, z_surf]
    emb_xs = [col_x0 + 0.3, col_x0 + 0.6, col_x1 - 0.2, col_x1 - 0.5]
    poly = plt.Polygon(list(zip(emb_xs, emb_ys)), fill=False,
                       edgecolor='#E07030', lw=1.5)
    ax.add_patch(poly)
    ax.text((col_x0 + col_x1) / 2, z_surf + 0.35, r'Area $S$',
            ha='center', va='center', fontsize=9, color='#E07030')

    # ── sensor triangles ─────────────────────────────────────────────────
    def sensor_triangle(y, label):
        cx = (col_x0 + col_x1) / 2
        tri = plt.Polygon([[cx-0.35, y-0.35], [cx+0.35, y-0.35], [cx, y+0.25]],
                          color='#3377BB', zorder=5)
        ax.add_patch(tri)
        ax.text(cx - 0.55, y, label, ha='right', va='center',
                fontsize=10, fontweight='bold', color='#3377BB')
        return cx

    cx1 = sensor_triangle(z_ac1, 'AC1')
    cx2 = sensor_triangle(z_ac2, 'AC2')
    cx3 = sensor_triangle(z_ac3, 'AC3')

    # ── horizontal sensor lines ───────────────────────────────────────────
    for z in [z_ac1, z_ac2, z_ac3]:
        ax.plot([col_x0, col_x1], [z, z], 'k-', lw=0.8)

    # ── layer height annotations ──────────────────────────────────────────
    x_ann = col_x0 - 0.2
    def brace(y1, y2, txt):
        ym = (y1 + y2) / 2
        ax.annotate('', xy=(x_ann, y1), xytext=(x_ann, y2),
                    arrowprops=dict(arrowstyle='<->', color='k', lw=0.8))
        ax.text(x_ann - 0.1, ym, txt, ha='right', va='center', fontsize=9)

    brace(z_ac1 - 0.25, z_ac2 + 0.25, r'$z_1 - z_2$')
    brace(z_ac2 - 0.25, z_ac3 + 0.25, r'$z_2 - z_3$')

    # ── midpoint dots ─────────────────────────────────────────────────────
    z_tau1 = (z_ac1 + z_ac2) / 2
    z_gamma23 = (z_ac2 + z_ac3) / 2
    for z in [z_tau1, z_gamma23]:
        ax.plot(col_x1, z, 'ko', markersize=5, zorder=6)
        ax.plot([col_x1, col_x1 + 0.15], [z, z], 'k-', lw=0.8)

    # ── right-side formula arrows ─────────────────────────────────────────
    x_arr_start = col_x1 + 0.3
    x_eq        = col_x1 + 0.5

    def formula_line(y, text, color='k', fontsize=10):
        ax.annotate('', xy=(x_arr_start, y), xytext=(col_x1 + 0.05, y),
                    arrowprops=dict(arrowstyle='->', color=color, lw=1.0))
        ax.text(x_eq, y, text, ha='left', va='center', fontsize=fontsize, color=color)

    # d1
    formula_line(z_ac1, r'$d_1 = \iint a_1\,dt$')

    # tau_1 — CORRECTED: single integral form (shear beam equation)
    formula_line(z_tau1,
                 r'$\tau_1(t) = \sum_i\,\rho_i\,h_i\,a_i(t)$',
                 color='#d62728', fontsize=9.5)

    # d2 — CORRECTED: added missing "=" sign
    formula_line(z_ac2, r'$d_2 = \iint a_2\,dt$')

    # gamma_23
    formula_line(z_gamma23,
                 r'$\gamma_{2/3} = \dfrac{d_2 - d_3}{\Delta z_{23}}$',
                 fontsize=9.5)

    # d3
    formula_line(z_ac3, r'$d_3 = \iint a_3\,dt$')

    # ── general formula box at bottom ─────────────────────────────────────
    box_y = 0.5
    ax.text(5.0, box_y,
            r'General:   $\tau(z_k,\, t) = \sum_{i:\,z_i > z_k}'
            r'\rho_i\,h_i\,a_i(t)$',
            ha='center', va='center', fontsize=10,
            bbox=dict(boxstyle='round,pad=0.4', fc='#FFFBE6', ec='#AAAAAA', lw=1.0))

    # ── correction notes ──────────────────────────────────────────────────
    note_x = 0.3
    ax.text(note_x, 1.8,
            'Corrections vs. submitted Figure 5:\n'
            u'  • τ₁ now uses correct discrete sum (not triple integral)\n'
            u'  • d₂ now includes "=" sign\n'
            u'  • General equation numbered as Eq. (2)',
            ha='left', va='top', fontsize=7.5,
            color='#555555',
            bbox=dict(boxstyle='round,pad=0.3', fc='#F0F0FF', ec='#AAAAAA', lw=0.8))

    # ── title ─────────────────────────────────────────────────────────────
    ax.set_title(
        'Figure 5 (revised): Procedure for shear strain and shear stress\n'
        'calculation from accelerometer data (Koga 1990; Watanabe 2023)',
        fontsize=11, pad=10)

    path = os.path.join(OUT_DIR, 'figure5_schematic_revised.pdf')
    fig.savefig(path, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"Saved: {path}")
    return path


if __name__ == '__main__':
    draw_schematic()
