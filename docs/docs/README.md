# FS Thesis — Predicting diagnosis risk from demographics

Short and practical repository for the master's thesis: evaluate how well tabular foundation models and baselines predict diagnosis risk using demographic features from MIMIC‑IV.
With information Patients can provide in the waiting room.

## Overview

### Quick Facts
- **Goal:** Measure predictive performance of foundation/tabular models (TabPFN, CatBoost, etc.) using only demographic features.
- **Data:** MIMIC‑IV (local CSVs in `files/…`) — original source: [PhysioNet MIMIC-IV](https://physionet.org/content/mimiciv/3.1/)
- **Core Analysis:** Jupyter notebooks in `notebooks/` provide ingestion, DuckDB views, and basic EDA.

## Resources
- [MIMIC Documentation](https://mimic.mit.edu/docs/)
- [TabPFN Repository](https://github.com/PriorLabs/TabPFN)

## Next Steps
For installation and setup instructions, please refer to the [Getting Started](getting-started.md) guide.