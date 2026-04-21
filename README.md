# Embankment Seismic Response: 2D vs 3D — Shaking Table Analysis Scripts

**Paper:** *3D and 2D Embankment Behaviour under Seismic Loading: Experimental Insights from 1-g Shaking Table Tests on Liquefiable Ground*
**Authors:** Zafar Avzalshoev, Pang-jo Chun — Institute of Engineering Innovation, The University of Tokyo

---

## Overview

This repository contains the analysis scripts and revised figures produced during the peer-review revision of the above manuscript. The study compares the dynamic response of an embankment on liquefiable sand under:

- **Case 3** — 3D straight embankment (wide container, 2200 × 1970 × 800 mm)
- **Case 4** — 3D L-shaped embankment (wide container, 2200 × 1970 × 800 mm)
- **Case 7** — 2D plane-strain embankment (narrow container, 2820 × 400 × 800 mm)

All tests used Silica Sand No. 7 at relative density D_r ≈ 52%, with a 200 mm liquefiable foundation layer and a 200 mm embankment, subjected to 5 Hz sinusoidal base excitation in four progressive shaking stages.

> **Note:** Raw experimental data (accelerometer time series, pore pressure records) are not included in this repository as they are part of an ongoing publication. Contact the corresponding author for data access requests.

---

## Repository Structure

```
├── scripts/
│   ├── generate_aligned_timeseries.py   # Time-aligned r_u figures (Reviewer C14)
│   ├── generate_corrected_loops.py      # Corrected τ–γ hysteresis loops (Reviewer C17)
│   ├── generate_epwp_acc_crossplot.py   # EPWP vs acceleration cross-plot (Reviewer C13)
│   ├── generate_figure5_schematic.py    # Corrected shear-beam schematic (Reviewer C11)
│   └── verify_tau_gamma.py              # Unit-check script for shear strain calculation
├── figures/
│   ├── aligned_freefield_ru.pdf         # Time-aligned free-field r_u (all cases)
│   ├── aligned_toe_ru.pdf               # Time-aligned toe r_u (all cases)
│   ├── aligned_embankment_ru.pdf        # Time-aligned under-embankment r_u (all cases)
│   ├── aligned_ru_combined.pdf          # 3-panel combined r_u comparison
│   ├── epwp_acc_crossplot.pdf           # EPWP spikes vs acceleration (3 cases)
│   ├── epwp_acc_case7_detail.pdf        # Case 7 Stage 4 spike detail
│   ├── figure5_schematic_revised.pdf    # Corrected shear-beam calculation schematic
│   ├── loops_under_embankment.pdf       # τ–γ loops beneath embankment crest
│   ├── loops_at_toe.pdf                 # τ–γ loops at embankment toe
│   └── loops_combined.pdf              # Side-by-side τ–γ comparison (all cases)
```

---

## Key Methods

### Shear-beam analysis (Koga 1990; Watanabe 2023)

Shear stress and strain at depth z_k are computed from accelerometer arrays:

```
τ(z_k, t) = Σᵢ  ρᵢ hᵢ aᵢ(t)     [sum over layers above z_k]
γ(t)       = (dᵢ − dⱼ) / Δzᵢⱼ   [relative displacement / layer height]
dᵢ(t)      = ∬ aᵢ(t) dt²         [double integration of acceleration in m/s²]
```

**Critical implementation note:** Accelerations must be converted from *g* to m/s² before integration. Omitting this conversion causes shear strains to be underestimated by a factor of 9.81.

### Excess pore pressure ratio

```
r_u = Δu / σ′_v0
```

Baseline u₀ is the mean pore pressure during the 1-second pre-shaking window. σ′_v0 values: 1.4 kPa (free-field/toe, 25 mm depth), 4.1 kPa (beneath embankment crest, 25 mm depth).

### Time alignment

All cases are referenced to a common relative time axis:
```
t_rel = t − t_onset
```
Onset times: Case 3 = 11.74 s, Case 4 = 14.18 s, Case 7 = 15.46 s.

---

## Corrections Applied

| Issue | Original | Corrected |
|-------|----------|-----------|
| τ–γ loop scale | Acceleration used in g → γ was 9.81× too small | Converted to m/s² before integration |
| Figure 5 τ₁ formula | Triple integral ∭ | Discrete sum Σᵢ ρᵢ hᵢ aᵢ(t) |
| Figure 5 d₂ | Missing "=" sign | d₂ = ∬ a₂ dt |
| Time alignment | Absolute time axis | Relative time t − t_onset |
| Case labels | Case A/B/C (inconsistent) | Case 3/4/7 throughout |

---

## Dependencies

```bash
pip install numpy pandas matplotlib scipy openpyxl
```

All scripts use standard scientific Python. Figures are saved as vector PDF (no rasterisation).

---

## Citation

If you use these scripts or figures, please cite the manuscript (citation will be updated upon acceptance):

> Avzalshoev, Z., Chun, P.-J. (2026). *3D and 2D Embankment Behaviour under Seismic Loading: Experimental Insights from 1-g Shaking Table Tests on Liquefiable Ground.* (under revision).

---

## Contact

Zafar Avzalshoev — zavzalshoev@gmail.com
Institute of Engineering Innovation, The University of Tokyo
