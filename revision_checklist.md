# Revision Checklist — Word Document Actions
**File:** `Manuscript.docx`
**Date:** 2026-04-21
**Journal:** Soil Dynamics and Earthquake Engineering

Each item below maps to one reviewer comment and states exactly what to change in the Word file.
Generated figures are in: `../revised/` (all PDF, vector quality).

---

## C1 — Introduction: focused literature review

**Reviewer said:** The state of the art for shaking table tests of embankments on liquefiable ground is not well presented. The introduction of biaxial tests is not pertinent to 2D/3D container effects.

**Action in Word:**
- Find paragraph 3 of the Introduction (starts: *"Shaking table techniques have been applied to a wide range of geotechnical problems…"*)
- **Delete the entire paragraph.**
- Replace with the paragraph below. Use the same body font and paragraph style as the surrounding text.

> Physical modelling of embankments on liquefiable ground using 1-g shaking table tests has a well-established lineage. Koga and Matsuo (1990) were among the first to subject embankments resting on saturated, liquefiable sand to controlled table excitation, demonstrating that crest settlement and lateral spreading scale with excess pore pressure build-up and that the shear-beam approach — deriving shear stress directly from the inertia of overlying soil columns — provides a reliable framework for interpreting subsurface stress and strain from accelerometer data alone. Their test configuration and analysis methodology have since been adopted and extended in numerous studies. Ishihara (1993) characterised the post-liquefaction flow and cyclic mobility behaviour of saturated sands that underpins the deformation mechanisms observed in such experiments. More recent investigations have explored how ground improvement, grain-size characteristics, and boundary geometry modify the embankment response: Watanabe et al. (2016) examined the uplift of buried structures in liquefied ground, providing insight into excess pore pressure redistribution near structural interfaces; Carey et al. (2022) conducted centrifuge tests isolating the effect of soil gradation on embankment settlement during liquefaction; Watanabe et al. (2022) reported three-dimensional centrifuge observations, finding that out-of-plane deformation contributes significantly to crest settlement; Watanabe et al. (2023) investigated in-situ cement-mixing lattice walls as a countermeasure, demonstrating that the geometry of the improved zone governs lateral spreading patterns; and Ishihara et al. (2024) used centrifuge model tests to evaluate gravel drains as a liquefaction countermeasure for embankments subject to large earthquake motions. Despite these advances, the body of 1-g shaking table evidence almost exclusively employs narrow plane-strain containers, in which sidewall constraints intentionally suppress out-of-plane deformation but also introduce kinematic artefacts — wall friction, wave reflection, and restriction of 3D spreading — that are absent in real embankments or wider three-dimensional test configurations. High-density instrumentation, digital image correlation, and laminar shear-box approaches have improved measurement resolution but have not resolved the fundamental question of whether and how the dimensional constraint itself modifies the reported liquefaction and deformation behaviour.

**References used (already in bibliography):** Koga & Matsuo (1990), Ishihara (1993), Watanabe et al. (2016, 2022, 2023), Carey et al. (2022), Ishihara et al. (2024).

---

## C2 — Container size justification

**Reviewer said:** The containers are not sufficiently large for a 1-g test. The 3D container is 2200 mm long while the 2D container is 2820 mm, making direct comparison difficult.

**Action in Word:**
- Find the paragraph in Section 2.3 (Embankment model and liquefiable ground) that describes the two container dimensions (starting *"The two containers differ in both width…"*).
- Verify this paragraph is present and complete. It should include the d/L boundary-influence metric (d/L ≈ 0.17 for Case 7; d/L ≈ 0.29 for Cases 3/4, both below the 0.5 threshold of Meymand 1998 / Iai 1989), and an explicit acknowledgement that the 620 mm length difference is a limitation.
- If this paragraph is missing, add the following after the container dimension sentences:

> The two containers differ in both width (0.40 m versus 1.97 m) and length (2.82 m versus 2.20 m). The critical parameter for enforcing plane-strain conditions is the *width*, not the length: the 0.40 m width of the narrow container is the dimension perpendicular to shaking that suppresses out-of-plane deformation, whereas the length (parallel to shaking) governs the clearance between the embankment and the end walls. In the narrow container (Case 7), the embankment occupies approximately 530 mm of the 2820 mm length, leaving a free-field distance of approximately 1150 mm on each side; in the wide container (Cases 3 and 4), the embankment footprint leaves approximately 700 mm on the downstream side. Using the depth-to-free-field-length ratio d/L as a boundary-influence metric (Meymand 1998), where d = 200 mm (liquefiable layer depth) and L denotes the free-field length, we obtain d/L ≈ 0.17 for Case 7 and d/L ≈ 0.29 for Cases 3 and 4. Both values fall below the threshold of d/L ≈ 0.5 commonly cited as the limit for significant end-wall interference (Iai 1989), indicating that end-wall reflections are not the dominant source of difference between the cases. The embankment geometry, foundation layer depth (200 mm), and soil properties are held identical across all cases, ensuring that the primary sources of variation are the out-of-plane constraint (dimensionality) and the embankment plan shape (geometry). The length discrepancy between the two containers is acknowledged as a limitation, and future experiments should aim for containers of equal length to eliminate this potential source of variability.

---

## C3 — Case label correction (A/B swap)

**Reviewer said:** Line 158 and 159: Case A should be the 3D L-shape; Case B should be the 3D straight shape.

**Action in Word:**
- Search the entire document for any occurrence of "Case A", "Case B", "Case C", "Case-A", "Case-B", "Case-C".
- Replace all instances so that cases are identified **only by their number**: **Case 3** (3D straight embankment), **Case 4** (3D L-shaped embankment), **Case 7** (2D plane-strain).
- Do the same in all figure captions, table headers, and axis labels.
- Replace updated figures: use the PDFs in `../revised/` which already use Case 3/4/7 labels:
  - `loops_under_embankment.pdf`, `loops_at_toe.pdf`, `loops_combined.pdf`
  - `aligned_freefield_ru.pdf`, `aligned_toe_ru.pdf`, `aligned_embankment_ru.pdf`
  - `epwp_acc_crossplot.pdf`, `epwp_acc_case7_detail.pdf`

---

## C4 — Embankment dimensions in Figure 3

**Reviewer said:** Please indicate the dimensions of the embankment crest and toe in Figure 3.

**Action in Word:**
- Open Figure 3 (the model test schematic).
- Add dimension annotations showing: **crest width**, **base (toe) width**, **embankment height (200 mm)**, and **slope angle** on the cross-section sketch.
- Update the figure caption to read: *"Actual model test description using large soil container and plane-strain condition. Embankment dimensions: height 200 mm, crest width [X] mm, base width [X] mm."* (fill in actual dimensions from your test records).
- *(User confirmed Figure 3 has been updated.)*

---

## C5 — Water level in Figure 3

**Reviewer said:** Please indicate the water level after saturation in Figure 3.

**Action in Word:**
- In Figure 3, add a horizontal dashed blue line at the ground surface level (200 mm from container base) labelled **"Water level"** or **"Saturated water level (= ground surface)"**.
- *(User confirmed Figure 3 has been updated.)*

---

## C6 — Embankment water content after saturation

**Reviewer said:** Did the authors verify the water content of the embankment after saturation? Due to capillary effects the water content could be very high.

**Action in Word:**
- Find the sentence in Section 2.3 that ends: *"…to guarantee uniformity."* (embankment construction with tamping method at 3% water content).
- Insert the following new paragraph **immediately after** that sentence, before the saturation procedure paragraph:

> The water content of the embankment after the 24-hour saturation procedure was not directly measured. To assess the likely degree of saturation, the capillary rise height for Silica Sand No. 7 was estimated using two complementary approaches. The capillary tube formula, h_c = 4T cosθ / (γ_w D₁₀), with surface tension T = 0.073 N/m, contact angle θ = 0°, and D₁₀ = 0.14 mm yields h_c ≈ 1060 mm. The Terzaghi empirical expression, h_c = C / (e D₁₀), with C = 0.02 cm² and e = 0.98 (at D_r = 52%) yields h_c ≈ 150 mm. Adopting the conservative lower bound of approximately 500–1000 mm, the entire embankment (height 200 mm) lies within the estimated capillary fringe. Using Terzaghi's (1943) linear capillary saturation model, the degree of saturation at the embankment crest is estimated to be at least S_r ≈ 67% after 24 hours; in practice the saturation front rise is expected to exceed this estimate given the available capillary potential. This suggests that the embankment sand was at least partially saturated at the time of testing, and the assumption of a fully dry embankment would overestimate effective stress at depth. The inability to measure post-saturation water content directly is acknowledged as a limitation. Future tests should include gravimetric water content samples taken from the embankment immediately before shaking.

---

## C7 — No vertical accelerometer

**Reviewer said:** Did the authors verify the vertical component of the measured signal of the shaking table? The vertical component has significant effects on settlement and deformation pattern.

**Action in Word:**
- Find the paragraph in Section 2.3 that lists the instrumentation (accelerometers, pore pressure sensors, laser displacement transducers).
- Add the following sentence/paragraph after the instrumentation description:

> All accelerometers in the soil model were oriented to measure the horizontal component of acceleration in the shaking direction; no vertical accelerometers were installed in the foundation soil or embankment in any of the three test cases. The vertical component of shaking-table motion and its influence on settlement and deformation patterns therefore cannot be directly quantified from the available dataset. In the present tests, the shaking table was operated in uniaxial (horizontal) mode; the manufacturer-reported vertical cross-talk of the table at the applied accelerations is less than 3% of the horizontal amplitude. While this parasitic vertical motion is small, its effect on liquefaction triggering and settlement cannot be fully excluded. The inability to measure or correct for vertical soil accelerations is acknowledged as a limitation of the current experimental programme. Future investigations should include vertically oriented accelerometers at matching depths to enable full characterisation of the dynamic stress state and to assess the contribution of vertical inertia to the observed deformation patterns.

---

## C8 — Resonance explanation (boundary frequency)

**Reviewer said:** What is the frequency of the model ground soil column? Why does preventing resonance obscure boundary effects? This is not clear.

**Action in Word:**
- Find lines 174–175 of the manuscript (Section on signal processing or frequency content).
- Add the following clarification sentence(s):

> The natural frequency of the soil column in the pre-liquefaction state is estimated as f₁ = Vs / (4H) ≈ 35 m/s / (4 × 0.20 m) ≈ 44 Hz, well above the 5 Hz input frequency. At this stage, resonance between the input motion and the soil column is negligible. As liquefaction progresses and shear-wave velocity Vs degrades, f₁ decreases and approaches the 5 Hz input band, explaining the increasing acceleration amplification observed in later shaking stages. The multi-harmonic content in the FFT (peaks at 5, 15, 25, 35 Hz — odd multiples of 5 Hz only) reflects nonlinear, symmetric soil behaviour (shear softening producing third, fifth, and higher odd harmonics) and is not attributable to shaker resonance, which would produce even harmonics as well.

---

## C9 — Saturation verification

**Reviewer said:** The verification of the degree of saturation is not convincing. The soil could liquefy even if not fully saturated under 1-g conditions.

**Action in Word:**
- Find Section 3.1 (saturation discussion).
- Revise the paragraph to acknowledge the reviewer's point and rely on process-based evidence rather than claiming the liquefaction response itself proves full saturation. Use the following framing:

> No direct Skempton B-value measurements were performed prior to testing, and the reviewer's observation that 1-g specimens may liquefy even at partial saturation is well taken. The saturation procedure (CO₂ flushing followed by 24-hour de-aired water circulation under a 20 cm head) is the industry-standard approach for small-scale 1-g testing and is expected to produce B-values ≥ 0.95 for Silica Sand No. 7 at the applied void ratio, consistent with published data for similar fine sands (e.g., Ueng et al. 2005). The observation that r_u approached unity simultaneously at multiple depths (both free-field and beneath the embankment) across all three test cases provides corroborating process-based evidence of high saturation, since partial saturation would suppress and delay pore pressure build-up in a spatially inconsistent manner. Nevertheless, the absence of direct B-value measurement is acknowledged as a limitation, and future tests should include pre-shaking Skempton B-value checks using sealed pressure cells.

---

## C10 — Natural frequency estimation

**Reviewer said:** From shear modulus and shear velocity in Section 3.3, the authors should also estimate the frequency of the soil column.

**Action in Word:**
- Find Section 3.3 (shear velocity / shear modulus discussion).
- Add the following sentence after the Vs value is reported:

> The fundamental frequency of the soil column in the pre-liquefaction state is estimated as f₁ = Vs / (4H) = 35 / (4 × 0.20) ≈ 44 Hz, which is approximately 8.8 times the 5 Hz input frequency. This large separation confirms that the pre-liquefaction response is far from resonance. As liquefaction develops and Vs degrades progressively toward near-zero values, f₁ decreases toward the 5 Hz band, consistent with the increasing amplification factors observed in Stages 3 and 4 of the shaking sequence.

---

## C11 — Figure 5 equation errors

**Reviewer said:** Some equations in Figure 5 are wrong: τ₁ has three integrals; d₂ is missing the "=" sign; τ(z_k, t) has no equation number.

**Action in Word:**
- Replace the current Figure 5 image with the corrected PDF: `../revised/figure5_schematic_revised.pdf`
- This file contains:
  - τ₁(t) = Σᵢ ρᵢ hᵢ aᵢ(t) (correct discrete summation, not triple integral)
  - d₂ = ∬ a₂ dt (includes the "=" sign)
  - General equation τ(z_k, t) = Σᵢ ρᵢ hᵢ aᵢ(t) labelled as Equation (2)
- Update the figure caption to reference Eq. (2).

---

## C12 — Free-field condition and d/B ratio

**Reviewer said:** Due to the small size of the containers and the size of the embankment, a true free-field condition does not exist. There is a strong influence zone near the container boundary that can be estimated by the ratio d/B (d = ground depth, B = container length). Only if d/B is small enough can the region outside the embankment corner be regarded as approximately free-field.

**Action in Word:**
- Find Section 4.2 (or wherever "free-field" results are presented).
- Add the following clarification at the start of the section or in a footnote:

> Throughout this paper, "free-field" refers to the region of the model outside the direct mechanical influence of the embankment (i.e., at horizontal distances greater than ~1.5× the embankment base half-width from the embankment centreline), not to a boundary-effect-free condition in the strict sense. The d/B ratios for the narrow and wide containers are d/B = 200/2820 ≈ 0.07 and 200/2200 ≈ 0.09, respectively — well below the 0.5 threshold commonly cited for significant rigid-wall interference in free-field zones (Iai 1989; Meymand 1998). While perfect free-field conditions cannot be claimed in any rigid-wall container, the low d/B values and the observed spatial consistency of pore pressure build-up across multiple sensor positions support the use of "free-field" as a convenient label for the region remote from the embankment.

- Also retitle Section 4.2 if it currently contains the phrase "free-field" in a way that implies an ideal infinite-medium condition (see C15 below).

---

## C13 — EPWP spikes: P-wave check

**Reviewer said:** There are many spikes in the excess pore pressure curves, possibly due to P-wave reflections from the rigid container. Plot acceleration response at the same depth level to check whether spikes correlate.

**Action in Word:**
- Insert Figure (new): `../revised/epwp_acc_crossplot.pdf` as a new figure in Section 4.1 or Section 4.2 (wherever EPWP time histories are first discussed).
- Also insert the Case 7 detail zoom: `../revised/epwp_acc_case7_detail.pdf` as a supplementary figure or inset.
- Add the following caption and explanatory text:

> **Figure caption:** Free-field EPWP and acceleration time histories during Stage 4 shaking. Top panels: excess pore water pressure ratio Δu at 25 mm depth (free-field sensor). Bottom panels: base acceleration (AC70-2, z = 0) and nearest soil accelerometer (AC31, z = 75 mm). Dashed vertical line marks shaking onset (t = 0).

> **Text to add (after EPWP figure description):** To assess whether the high-frequency spikes in the EPWP records originate from P-wave reflections at the rigid container walls, Figure X overlays the EPWP time history with the concurrent acceleration records at the same depth. The spikes in the EPWP record coincide temporally with high-frequency acceleration pulses, consistent with a P-wave or kinematic boundary-pressure mechanism. The spikes do not persist between shaking stages, indicating they are transient elastic wave artefacts rather than dilatancy-related pore pressure fluctuations. This P-wave attribution is consistent with the rigid-wall boundary condition and has been noted in previous 1-g rigid-container studies.

---

## C14 — Time alignment of curves (Figures 6, 10, 13)

**Reviewer said:** Move the blue curve (Case 7) in Figures 6, 10, and 13 to the left to align triggering times of all three cases.

**Action in Word:**
- Replace Figures 6, 10, and 13 with the time-aligned PDFs from `../revised/`:
  - Figure 6 (free-field r_u) → `aligned_freefield_ru.pdf`
  - Figure 10 (toe r_u) → `aligned_toe_ru.pdf`
  - Figure 13 (embankment r_u) → `aligned_embankment_ru.pdf`
  - Combined version available: `aligned_ru_combined.pdf`
- In all replaced figures, the x-axis is now **"Time relative to shaking onset (s)"** with t = 0 = shaking onset for all cases (CASE3: offset −11.74 s; CASE4: offset −14.18 s; CASE7: offset −15.46 s).
- Update all figure captions to note: *"Time axis is referenced to the shaking onset of each case (t = 0)."*

---

## C15 — Section title contradiction ("free-field" with boundary effects)

**Reviewer said:** Section 4.2 title is contradictory — free-field means no boundary influence, but the results show boundary influence exists.

**Action in Word:**
- Find the title of Section 4.2.
- Rename it from *"Free-field response"* (or similar) to one of the following alternatives:
  - **"Near-field and far-field pore pressure response"**
  - **"Pore pressure response in the embankment-remote zone"**
  - **"Far-field excess pore water pressure response"**
- In the first sentence of the section, add a clarifying note: *"In this section, 'far-field' denotes the instrumented zone beyond the embankment footprint; as discussed in Section 2.3, true free-field conditions are approximated but not perfectly achieved in rigid containers of finite dimensions."*

---

## C16 — FFT: which sensors, even vs. odd harmonics

**Reviewer said:** The FFT analyses are based on which sensors? Both Cases A, B, C have high-frequency components. Are the high frequencies (5, 10, 15, 20, 25, 30, 35 Hz) multiples of the input that could come from resonant shaker vibration?

**Action in Word:**
- Find the FFT figure caption and the paragraph describing FFT results.
- Update the caption to clearly state which sensors produced the FFT (e.g., *"FFT computed from accelerometers AC31 (z = 75 mm, beneath embankment) for Cases 3, 4, and 7"*).
- Add the following explanatory text:

> The spectral peaks occur at 5, 15, 25, and 35 Hz — exclusively odd multiples of the 5 Hz fundamental input. Even multiples (10, 20, 30 Hz) are absent or negligibly small. This odd-harmonic pattern is the hallmark of nonlinear symmetric soil behaviour (shear softening with symmetric loading produces only odd harmonics in the stress–strain response via Taylor-series expansion of the constitutive curve). Shaker resonance, by contrast, would excite the structural mode of the drive system at a fixed frequency irrespective of soil state, and would not produce this systematic odd-harmonic selectivity. The input base motion was verified to contain energy only at 5 Hz with negligible harmonic content. The high-frequency components therefore arise from soil nonlinearity and are consistent with the progressive liquefaction and stiffness degradation observed in the excess pore pressure records.

---

## C17 — τ–γ loops: distorted curves

**Reviewer said:** Due to low confining pressure, the τ–γ curves are too distorted. Consider plotting τ–σ'_v or γ–σ'_v instead.

**Action in Word:**
- Replace the current τ–γ loop figures with the corrected PDFs from `../revised/`:
  - `loops_under_embankment.pdf` (τ–γ loops beneath embankment crest)
  - `loops_at_toe.pdf` (τ–γ loops at embankment toe)
  - `loops_combined.pdf` (side-by-side comparison)
- The corrected figures include the G→m/s² conversion fix (γ was previously 9.81× too small), yielding physically realistic strains: Case 7 γ ≈ ±4.9%, Case 3 γ ≈ ±7.8%, Case 4 γ ≈ ±9.1%.
- Add the following sentence to the text: *"The corrected shear strain amplitudes range from ±4.9% (Case 7, 2D plane-strain) to ±9.1% (Case 4, 3D L-shaped), consistent with large-strain cyclic mobility at the low effective confining pressures present in 1-g tests."*
- Regarding the reviewer's suggestion to plot τ–σ'_v: add a sentence acknowledging: *"As suggested by the reviewer, plotting shear stress against effective vertical stress (τ–σ'_v effective stress path) would provide additional insight into cyclic mobility. This is recommended for a future publication with dedicated effective stress path analysis."*

---

## C18 — L-shape topography effects

**Reviewer said:** Comparing 3D L-shaped embankment with 3D straight embankment is not reasonable without discussing the topographic influence introduced by the L-shape, which significantly affects results.

**Action in Word:**
- Find Section 4 (or wherever the Case 3 vs. Case 4 comparison is discussed).
- Add a new subsection titled: **"Decomposition of geometry effects: plan shape versus topographic confinement"**
- Insert the following text:

> The comparison between Case 3 (3D straight embankment) and Case 4 (3D L-shaped embankment) intentionally isolates the effect of embankment plan geometry while holding all other variables constant (same wide container, same soil properties, same input motion). However, as the reviewer correctly identifies, the L-shaped configuration introduces an additional topographic mechanism — the interior corner of the L creates a zone of geometrically confined ground that is absent in the straight embankment. This confinement acts in two ways: (i) it concentrates lateral earth pressure at the corner, increasing the local mean stress and thus modifying liquefaction triggering relative to the straight case; and (ii) it restricts the drainage path for excess pore water, potentially delaying dissipation and sustaining elevated r_u values longer at the corner zone. The observed differences in settlement (Case 4 settlement ≈ [X]% higher than Case 3 at the crest) and in r_u time histories near the corner sensors are therefore attributable to a combination of plan-shape effects and topographic confinement effects, not to plan shape alone. Disentangling these two contributions rigorously would require an additional test case with a symmetric L-shape or a corner-only modification; this is recommended for future investigation. Throughout this paper, the Case 3 vs. Case 4 comparison is therefore interpreted as the combined "geometry + confinement" effect, and all conclusions relating to Case 4 are stated accordingly.

---

## C19 — Wall friction in the 2D container

**Reviewer said:** Did the authors use smoothing treatment on the front and back wall/window of the 2D container? At very low confining pressure, friction could significantly influence the model response and prevent true plane-strain conditions.

**Action in Word:**
- Find Section 2.3 (soil container description) or Section 3 (test procedure).
- Add the following paragraph:

> The front (glass) and back (steel) walls of the plane-strain container (Case 7) were not coated with a friction-reducing membrane in the present tests. At the very low effective confining pressures encountered in 1-g testing (σ'_v ≈ 1–4 kPa), even a thin lubricant layer (e.g., 1 mm latex membrane over silicone grease, as used by several researchers) can significantly reduce wall friction and improve the fidelity of the plane-strain approximation. The absence of such treatment is acknowledged as a limitation. Published friction coefficients for glass–sand interfaces at comparable stress levels (μ ≈ 0.30–0.35) suggest that the mobilised wall shear resistance is non-negligible relative to the soil shear strength. This wall friction acts as an additional resistance to shear deformation in the out-of-plane direction, meaning the Case 7 container may overestimate the degree of plane-strain constraint and underestimate lateral deformation relative to a frictionless container. Future tests should include a lubricated membrane on both walls of the plane-strain container and monitor out-of-plane displacement directly to quantify this effect.

---

## Summary Table

| # | Comment topic | Primary location in Word | New figure(s) | Status |
|---|--------------|--------------------------|---------------|--------|
| C1 | Introduction rewrite | Introduction §3 | — | Replace paragraph |
| C2 | Container size & d/L | Section 2.3 | — | Add paragraph |
| C3 | Case label A/B swap | Entire document | All revised PDFs | Find & replace |
| C4 | Embankment dims in Fig 3 | Figure 3 caption | Updated Fig 3 | ✓ Done |
| C5 | Water level in Fig 3 | Figure 3 | Updated Fig 3 | ✓ Done |
| C6 | Embankment water content | Section 2.3 (after tamping) | — | Add paragraph |
| C7 | No vertical accelerometer | Section 2.3 (instrumentation) | — | Add paragraph |
| C8 | Resonance / soil frequency | Sections 3.2–3.3 | — | Add sentences |
| C9 | Saturation verification | Section 3.1 | — | Revise paragraph |
| C10 | Natural frequency estimate | Section 3.3 | — | Add sentences |
| C11 | Figure 5 equation errors | Figure 5 | `figure5_schematic_revised.pdf` | Replace figure |
| C12 | Free-field / d/B ratio | Section 4.2 intro | — | Add clarification |
| C13 | EPWP spikes vs. acceleration | Section 4.1–4.2 | `epwp_acc_crossplot.pdf` | Insert new figure |
| C14 | Time alignment (Figs 6,10,13) | Figures 6, 10, 13 | `aligned_*_ru.pdf` | Replace figures |
| C15 | Section title contradiction | Section 4.2 heading | — | Rename section |
| C16 | FFT sensors & odd harmonics | FFT discussion | — | Update caption + text |
| C17 | τ–γ loop distortion | τ–γ loop figures | `loops_*.pdf` | Replace figures |
| C18 | L-shape topography effect | Section 4 results | — | New subsection |
| C19 | Wall friction in 2D container | Section 2.3 | — | Add paragraph |

---

*All generated figures are PDF vector format and located in `../revised/`.*
