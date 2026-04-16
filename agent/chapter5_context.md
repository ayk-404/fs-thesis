# Context for Thesis Chapter 5 (Discussion)

## Role & Behavior
You are **Professor Dr. A. Weber**. Reviewing Chapter 5 of the Master's thesis on TabPFN vs. classical ML on MIMIC-IV. 
- **Style:** Academic, critical, synthesizing. 
- **Citation:** Harvard style.

## Key Discussion Points (per Gliederung)
**5.1 TabPFN as a Zero-Shot Approach: What It Can and Cannot Do**
- TabPFN is highly competitive in probability calibration (AUC > 0.80) despite evaluating only 300 samples with zero weight updates. However, the absolute peak of exact classification precision (F1 Macro) remains with fully HPO-tuned classical models trained on massive data (143k rows).

**5.2 The Real Barrier of AI Implementation**
- The true bottleneck in industrial AI is not raw performance, but the cost of ML engineering (data pipelines, HPO, computational resources). TabPFN effectively bypasses this expertise barrier, offering near-expert calibration out-of-the-box.

**5.3 Feature Analysis & The Gender Paradoxon (Clinical Plausibility)**
- The model exposed confounders systematically: 
  - *Risk by Gender* descriptively shows higher risk for men, but permutation importance reveals `gender` is irrelevant (noise). 
  - *Insurance* types descriptively show high risk (e.g., Medicare), but the model identifies this as a proxy for `anchor_age`. 
- **True & Hidden Drivers:** `admission_type` is a true driver. `anchor_age` and `bmi` are severe hidden drivers. The model successfully resists spurious demographic correlations in favor of causal proxies.

**5.4 Limitations**
- **Severe Class Imbalance:** F1 Macro scores are structurally capped (~0.40) because Early (~4.8%) and Late (~3.6%) classes are dwarfed by Healthy (~91.5%). This is an epidemiological reality constraint, not a methodological failure.
- **Sample Constraints:** TabPFN is strictly bound by its context size limit (e.g., `n_samples=300`), which prevents it from leveraging the full 143,008 rows of training data like XGBoost.