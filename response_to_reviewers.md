# Response to Reviewer Comments
**Manuscript title:** 3D and 2D Embankment Behaviour under Seismic Loading: Experimental Insights from 1-g Shaking Table Tests on Liquefiable Ground
**Journal:** Soil Dynamics and Earthquake Engineering
**Date of response:** April 2026

We sincerely thank the reviewer for the thorough and constructive critique of our manuscript. The comments have identified genuine weaknesses in the original submission, and we believe the revised manuscript is substantially improved as a result. Below we respond to each comment in turn. All changes in the manuscript are highlighted in the revised Word document. New figures are supplied as separate vector-PDF files.

---

## Comment 1
*"The state of the art of the development of the shaking table test of embankment on liquefiable ground is not well presented in the introduction part. The introduction of the bi-axial test is not very pertinent to the 2D or 3D effects induced by the containers."*

**Author Response:**

We agree entirely. The original introduction contained a broad survey of shaking table applications (tunnels, pile foundations, retaining walls, vibration mitigation, etc.) that was tangential to the specific problem of embankments on liquefiable ground, and the mention of biaxial tests added confusion rather than context.

**What has been done:** The broad survey paragraph has been deleted and replaced with a focused literature review tracing the lineage of 1-g shaking table tests of embankments on liquefiable ground specifically. The revised paragraph covers: Koga and Matsuo (1990) — who established the shear-beam methodology that underpins our analysis; Ishihara (1993) on post-liquefaction flow and cyclic mobility; Watanabe et al. (2016, 2022, 2023) on 3D embankment behaviour and ground improvement; Carey et al. (2022) on grain-size effects; and Ishihara et al. (2024) on countermeasure evaluation. The paragraph concludes by identifying the "dimensional validation gap" — the fact that nearly all 1-g shaking table evidence uses narrow plane-strain containers — which directly motivates the present study. Please see the revised Introduction, paragraph 3.

---

## Comment 2
*"The size of the containers used in this study is not sufficiently large for 1g shaking table test. In addition, the container for 3D study has a dimension of 2200 mm, and the container for 2D study has a dimension of 2820 mm. This difference makes the results not easy to compare."*

**Author Response:**

We acknowledge both the size concern and the length discrepancy. Container sizes in 1-g testing are constrained by laboratory infrastructure; we cannot retroactively enlarge the containers, but we can — and have — rigorously quantified the implications.

**What has been done:** A new paragraph has been added to Section 2.3 using the depth-to-free-field-length ratio d/L (Meymand 1998; Iai 1989) as a boundary-influence metric. With d = 200 mm (liquefiable layer depth) and free-field lengths L ≈ 1150 mm (Case 7) and ≈ 700 mm (Cases 3/4), we obtain d/L ≈ 0.17 and 0.29, respectively — both below the 0.5 threshold for significant end-wall interference. The critical comparison variable is the container *width* (0.40 m vs. 1.97 m, which enforces the plane-strain constraint), not the length. The 620 mm length discrepancy is acknowledged as a limitation and will be eliminated in future experiments. The embankment geometry, foundation depth (200 mm), and soil properties are identical across all cases, ensuring that dimensionality and plan geometry remain the primary variables.

---

## Comment 3
*"Line 158 and Line 159. Case A should be the 3D L shape; Case B should be the 3D straight shape."*

**Author Response:**

The reviewer has correctly identified an inconsistency in our labelling. In the original submission, "Case A" and "Case B" were assigned inconsistently, and the letters created ambiguity about which case represented which geometric configuration.

**What has been done:** To eliminate any possibility of confusion, we have removed the A/B/C letter designators entirely from the manuscript and all figures. Cases are now identified exclusively by their test number throughout all text, figures, tables, and captions:
- **Case 3** = 3D straight embankment (wide container)
- **Case 4** = 3D L-shaped embankment (wide container)
- **Case 7** = 2D plane-strain embankment (narrow container)

All revised figures in the supplementary PDF package use this consistent labelling.

---

## Comment 4
*"Please indicate the dimensions of the embankment crest and toe in Figure 3."*

**Author Response:**

**What has been done:** The embankment cross-section in Figure 3 has been updated to include annotated dimensions: crest width, base (toe) width, embankment height (200 mm), and slope angle. The figure caption has been updated accordingly.

---

## Comment 5
*"Please indicate the water level after the saturation in Figure 3."*

**Author Response:**

**What has been done:** A horizontal dashed line indicating the water level at the ground surface (z = 200 mm from the container base) has been added to Figure 3 with the label "Water level (= ground surface after saturation)."

---

## Comment 6
*"Did the authors verify the water content of the embankment after saturation? The height of the embankment is just 200 mm; due to the capillary effect, the water content of the embankment could be very high. Please add information on the water content of the embankment."*

**Author Response:**

This is a valid and important observation. The embankment water content after saturation was not directly measured in the original tests, which is a limitation we accept.

**What has been done:** We have added a paragraph to Section 2.3 reporting a capillary rise analysis for Silica Sand No. 7. Using the capillary tube formula (h_c = 4T cosθ / γ_w D₁₀ ≈ 1060 mm) and the Terzaghi empirical formula (h_c = C / (e D₁₀) ≈ 150 mm), the estimated capillary fringe height spans 150–1060 mm, conservatively bounded at 500–1000 mm. Since the entire embankment height (200 mm) lies within this range, significant capillary saturation of the embankment within the 24-hour saturation period is expected. Applying Terzaghi's linear capillary saturation model, the degree of saturation at the embankment crest is estimated at S_r ≥ 67%. The absence of direct water content measurements is acknowledged as a limitation, and we recommend gravimetric sampling immediately before shaking in future tests.

**What is not possible retroactively:** Direct gravimetric water content measurements cannot be obtained from the already-completed tests. The capillary analysis provides the best available retrospective estimate.

---

## Comment 7
*"Did the authors verify the vertical component of the measured signal of the shaking table? The vertical component has significant effects on the settlement and the deformation pattern of the embankment."*

**Author Response:**

We did not install vertical accelerometers in the soil model, and this is a genuine limitation of the experimental programme.

**What has been done:** A paragraph has been added to Section 2.3 explicitly stating: (i) all soil accelerometers measured horizontal acceleration only; (ii) the shaking table was operated in uniaxial (horizontal) mode with manufacturer-specified vertical cross-talk < 3% of horizontal amplitude; (iii) the effect of this parasitic vertical motion on liquefaction triggering and settlement cannot be fully excluded; and (iv) this is acknowledged as a limitation. Future investigations should include vertically oriented accelerometers at matched depths.

**What is not possible retroactively:** The tests have been completed; vertical soil acceleration records cannot be retrieved. The 3% cross-talk figure from the manufacturer specification represents the best available bound on vertical excitation.

---

## Comment 8
*"Line 174 and Line 175. What is the frequency of the model ground of the soil column? Why preventing the resonance effects could obscure the effect of the boundary? This is not clear."*

**Author Response:**

We agree that the original text was unclear on this point.

**What has been done:** Text has been added in the signal processing section providing a quantitative estimate of the pre-liquefaction fundamental frequency: f₁ = Vs / (4H) ≈ 35 / (4 × 0.20) ≈ 44 Hz. This is approximately 8.8 times the 5 Hz input frequency, confirming that pre-liquefaction resonance is negligible. The text also explains that as liquefaction progresses and Vs degrades, f₁ decreases toward the 5 Hz input band, consistent with the increasing amplification observed in Stages 3 and 4. The multi-harmonic FFT content (peaks at 5, 15, 25, 35 Hz — odd multiples only) is explained as arising from nonlinear symmetric soil response, not from shaker resonance.

---

## Comment 9
*"Section 3.1. The verification of the degree of saturation is not convincing. The degree of saturation is the initial state of the undisturbed soil, which cannot be judged by the liquidation of the soil under strong shearing deformation. Especially for the 1-g shaking table test, the soil could be easily liquefied, even if the soil is not fully saturated."*

**Author Response:**

We concede the reviewer's point. Using the occurrence of liquefaction as evidence of full saturation is circular reasoning under 1-g conditions, where low effective stress lowers the threshold for pore pressure build-up regardless of degree of saturation.

**What has been done:** Section 3.1 has been revised to remove the circular argument. The revised text: (i) explicitly acknowledges that no Skempton B-value measurements were made; (ii) notes that the CO₂-flush + 24-hour de-aired water circulation procedure is standard practice for achieving B ≥ 0.95 in similar fine sands (citing Ueng et al. 2005); (iii) offers the spatial consistency of r_u ≈ 1.0 across multiple independent sensors as corroborating process-based evidence (partial saturation would suppress pore pressure build-up inconsistently across depths and locations); and (iv) recommends sealed pressure-cell B-value checks in future tests.

---

## Comment 10
*"From the shear modulus and the shear velocity of the soil in section 3.3, the authors could also estimate the frequency of the soil column. This information is important, and the author could complete this information."*

**Author Response:**

**What has been done:** The natural frequency estimate has been added to Section 3.3: f₁ = Vs / (4H) = 35 / (4 × 0.20) ≈ 44 Hz pre-liquefaction, decreasing toward the 5 Hz input band as liquefaction-induced Vs degradation occurs. This information contextualises the FFT results and the progressive amplification patterns in Stages 3 and 4.

---

## Comment 11
*"Some equations in Figure 5 are wrong; please check. For example, why there are three integrals for tau_1? There is a '=' symbol missing for d₂, etc. In addition, equation tau(z_k,t) in the text has no equation number."*

**Author Response:**

The reviewer is correct on all counts. These were errors introduced during figure preparation.

**What has been done:** Figure 5 has been completely redrawn. The corrections are:
1. τ₁(t) = Σᵢ ρᵢ hᵢ aᵢ(t) — discrete summation replaces the erroneous triple integral.
2. d₂ = ∬ a₂ dt — the missing "=" sign has been added.
3. The general equation τ(z_k, t) = Σᵢ (zᵢ > z_k) ρᵢ hᵢ aᵢ(t) is now labelled as Equation (2) in the caption and cross-referenced in the text.

The corrected figure is provided as `figure5_schematic_revised.pdf`.

---

## Comment 12
*"Line 255. Due to the small size of the containers and considering the size of the embankment, the free-field condition does not exist either in the 3D or in the 2D models. There is a strong influence zone near the boundary of the container which can be estimated approximately as the ratio of d/B. d is the depth of the ground and B is the length of the container. If the d/B is small enough, then the zone outside the corner of the rigid container could be regarded as approximately free-field."*

**Author Response:**

The reviewer raises an important terminological and physical point.

**What has been done:** We have added a clarification at the beginning of Section 4.2 (previously titled "Free-field response") acknowledging that the term "free-field" in this context refers to the zone outside the mechanical influence zone of the embankment, not to an ideal infinite-medium condition. The d/B ratios are computed: d/B = 200/2820 ≈ 0.07 (Case 7) and 200/2200 ≈ 0.09 (Cases 3/4). Both are well below the 0.5 threshold (Iai 1989; Meymand 1998), indicating that the region beyond the embankment corner approximates free-field behaviour within the constraints of a rigid container. The section title has also been amended to "Far-field excess pore water pressure response" to avoid implying ideal free-field conditions (see also Comment 15).

---

## Comment 13
*"From the results of Figure 6, there are many spikes in the excess pore pressure curves, these may be due to the strong boundary effect of the rigid container, which reflects many P-waves. The authors could also plot the acceleration response at the same level to check if there are also P-wave induced spikes."*

**Author Response:**

This is an excellent suggestion. We carried out the requested analysis.

**What has been done:** A new figure has been added (Figure X: `epwp_acc_crossplot.pdf`) that overlays the EPWP time history at 25 mm depth with the concurrent base acceleration (AC70-2, z = 0) and the nearest soil accelerometer (AC31, z = 75 mm) for all three cases. A zoomed detail for Case 7 (the case with the most prominent spikes) is also provided (`epwp_acc_case7_detail.pdf`). The analysis confirms that the EPWP spikes coincide temporally with high-frequency acceleration pulses, consistent with a P-wave or kinematic boundary-pressure mechanism. The spikes are transient and do not persist between shaking stages, indicating they are elastic wave artefacts. This finding supports the reviewer's interpretation and the discussion has been updated accordingly. Importantly, the EPWP trend (build-up, stabilisation, and post-shaking dissipation) is not affected by the spike artefacts and the overall r_u evolution remains physically interpretable.

---

## Comment 14
*"The authors could move the blue curve in Figure 6 to the left to align with the other two curves. In this way, the three curves have the same triggering time. The same comment for Figure 10 and Figure 13."*

**Author Response:**

We thank the reviewer for this constructive suggestion. The three test cases were triggered at different absolute times (Case 3 at t = 11.74 s, Case 4 at t = 14.18 s, Case 7 at t = 15.46 s), making direct visual comparison difficult in the original figures.

**What has been done:** Figures 6, 10, and 13 have been replaced with time-aligned versions in which all curves are plotted on a common relative time axis t_rel = t − t_onset, so that t_rel = 0 corresponds to the shaking onset for each case. The shaking stage boundaries (Stages 1–4) are shown as vertical dashed lines on the common axis. All figure captions now state: *"Time axis is referenced to the shaking onset of each case (t = 0)."* The revised figures are: `aligned_freefield_ru.pdf`, `aligned_toe_ru.pdf`, `aligned_embankment_ru.pdf`.

---

## Comment 15
*"Section 4.2. The section title is contradictory, if a free-field condition exists in the model, it should not be influenced by the boundaries. The free-field condition means an idealized condition, where no boundary effect exists. If the response can be influenced by boundaries, then it is not the free-field condition."*

**Author Response:**

The reviewer's terminological critique is correct and well taken.

**What has been done:** Section 4.2 has been retitled from "Free-field response" to **"Far-field excess pore water pressure response"**. The opening sentence of the section now clarifies: *"In this section, 'far-field' denotes the instrumented zone beyond the embankment footprint; as discussed in Section 2.3, true free-field conditions are approximated but not perfectly achieved in rigid containers of finite dimensions."* This change is consistent with Comment 12.

---

## Comment 16
*"The FFT analyses are based on which sensors? Please indicate clearly. Both A, B and C have high frequency components; did the author verify the input signal? When looking at the frequencies, there are peaks at 5, 10, 15, 20, 25, 30, 35 etc. If the input signal has a frequency of 5 Hz, then the high frequencies are 2 times, 3 times, 4 times etc. of the input signal; they could come from the resonant vibration of the shaker. Please check that."*

**Author Response:**

We have carefully re-examined the spectral content.

**What has been done:** The FFT figure caption has been updated to specify which sensors produced the spectra (AC31, z = 75 mm beneath the embankment crest, for Cases 3, 4, and 7). Upon re-examination, the spectral peaks occur at **5, 15, 25, and 35 Hz only** — exclusively odd multiples of the 5 Hz fundamental. Even harmonics (10, 20, 30 Hz) are absent or negligibly small. The text now explains that this odd-harmonic pattern is the hallmark of nonlinear symmetric soil behaviour: shear softening with symmetric cyclic loading produces only odd harmonics through the Taylor expansion of the constitutive curve. In contrast, shaker resonance would excite a structural mode at a fixed frequency irrespective of soil state and would not produce systematic odd-harmonic selectivity. The input base motion was verified to contain energy at 5 Hz with negligible harmonic content (checked via AC70-2, the base accelerometer on the table platform). The high-frequency spectral content therefore arises from soil nonlinearity consistent with progressive liquefaction, not from shaker resonance.

---

## Comment 17
*"Due to the low confining pressure, the curves of tau-gamma for the shear stress and strain analysis are not convincing. These curves are too distorted, which makes it very difficult to read. Instead of the tau-gamma curves, the authors could consider plotting the tau-sigma_v' curve or gamma-sigma_v' curves."*

**Author Response:**

We identified the root cause of the excessive distortion: in the original analysis code, the accelerations were used in units of g (gravitational acceleration) in the cumulative trapezoidal integration for displacement, without conversion to m/s². This produced shear strains γ that were 9.81 times smaller than the correct values, compressing the horizontal axis and making the loops appear nearly vertical.

**What has been done:** The code has been corrected to convert accelerations from g to m/s² (multiplying by 9.81) before integration. The corrected shear strain amplitudes are: Case 7 γ ≈ ±4.9%, Case 3 γ ≈ ±7.8%, Case 4 γ ≈ ±9.1%. These values are physically consistent with large-strain cyclic mobility at the low effective confining pressures present in 1-g tests. The revised loop figures (`loops_under_embankment.pdf`, `loops_at_toe.pdf`, `loops_combined.pdf`) show well-formed hysteresis loops with clear energy dissipation and progressive stiffness degradation.

**Regarding the suggestion to plot τ–σ'_v:** We acknowledge this would provide additional insight into cyclic mobility and effective stress path evolution. Given the significant revision work already undertaken and the limitations of the 1-g stress state, we have added a sentence recommending τ–σ'_v effective stress path plots as a priority for a future dedicated publication.

---

## Comment 18
*"The comparison of the 3D L shape embankment with the 3D straight embankment is not reasonable, since the 3D L shape embankment introduces another important topography issue, which will influence the results significantly, and needs to be discussed in the interpretation of the results."*

**Author Response:**

This is a fundamental and correct observation that the original manuscript did not adequately address.

**What has been done:** A new subsection has been added in Section 4 titled **"Decomposition of geometry effects: plan shape versus topographic confinement"**. This subsection:
1. Acknowledges explicitly that the L-shaped embankment introduces a topographic confinement effect at the interior corner that is absent in the straight embankment.
2. Explains the two mechanisms by which confinement acts: (i) concentration of lateral earth pressure at the corner, which modifies liquefaction triggering; and (ii) restriction of drainage paths, which sustains elevated r_u values longer at the corner zone.
3. States clearly that the observed Case 3 vs. Case 4 differences reflect both plan-shape effects and topographic confinement effects combined, and that rigorous separation would require an additional test case (e.g., a symmetric corner configuration).
4. Recommends this separation as a priority for future investigation.
5. Revises all conclusions relating to Case 4 to be interpreted as the combined "geometry + confinement" effect.

---

## Comment 19
*"Did the author use some smoothing treatment on the front and back wall/window of the 2D container? For such a test with very low confining pressure, the friction could influence the response of the model greatly. To well reproduce the 2D plane strain condition, the sidewall of the container should be smooth enough to allow the deformation of the soil."*

**Author Response:**

No friction-reducing membrane was applied to the walls of the plane-strain container in the present tests. We accept this as a limitation.

**What has been done:** A paragraph has been added to Section 2.3 explicitly stating: (i) no lubricant coating or membrane was used on the glass front wall or steel back wall of the Case 7 container; (ii) at the low effective confining pressures of 1-g testing (σ'_v ≈ 1–4 kPa), glass–sand friction coefficients (μ ≈ 0.30–0.35) mean that mobilised wall shear resistance is non-negligible relative to soil shear strength; (iii) this wall friction likely overestimates the degree of plane-strain constraint and underestimates lateral deformation in Case 7 relative to an ideal frictionless container; (iv) future tests should use a 1 mm latex membrane over silicone grease on both walls, which is the standard practice for minimising wall friction in narrow plane-strain containers, and should monitor out-of-plane displacement directly to quantify any residual influence.

**What is not possible retroactively:** The tests have been completed and the wall friction effect cannot be removed from the existing dataset. However, the direction of the bias is known — wall friction in Case 7 suppresses lateral deformation, meaning the true dimensionality effect (3D settlement > 2D settlement) would be even larger than reported here if wall friction were eliminated. The qualitative conclusions of the study therefore remain valid and are conservative.

---

## Summary of Changes

| Comment | Addressed? | Type of change |
|---------|-----------|----------------|
| C1 | Yes | Introduction paragraph replaced |
| C2 | Yes | New justification paragraph + d/L calculation |
| C3 | Yes | All A/B/C labels replaced by Case 3/4/7 throughout |
| C4 | Yes | Figure 3 updated with dimensions |
| C5 | Yes | Figure 3 updated with water level |
| C6 | Yes | New paragraph on capillary saturation analysis |
| C7 | Yes | Limitation paragraph added; measurement gap quantified |
| C8 | Yes | Natural frequency and harmonic analysis added |
| C9 | Yes | Saturation argument revised; circular logic removed |
| C10 | Yes | f₁ ≈ 44 Hz estimate added to Section 3.3 |
| C11 | Yes | Figure 5 redrawn with all corrections |
| C12 | Yes | d/B ratio computed; "far-field" terminology clarified |
| C13 | Yes | New figure: EPWP vs. acceleration cross-plot |
| C14 | Yes | Figures 6, 10, 13 replaced with time-aligned versions |
| C15 | Yes | Section 4.2 retitled to "Far-field EPWP response" |
| C16 | Yes | Sensor IDs specified; odd-harmonic analysis added |
| C17 | Yes | Bug fixed (G→m/s²); loops redrawn; τ–σ'_v suggested for future work |
| C18 | Yes | New subsection on plan-shape vs. topographic confinement |
| C19 | Yes | Limitation acknowledged; friction magnitude estimated; future remedy described |

We believe the revised manuscript addresses all 19 comments substantively. We are grateful for the detailed review, which has materially strengthened the scientific rigour and transparency of the work.

---

*Corresponding author: Zafar Avzalshoev, Institute of Engineering Innovation, The University of Tokyo*
*Email: zavzalshoev@gmail.com*
