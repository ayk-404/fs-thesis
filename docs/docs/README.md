# FS Thesis — Predicting diagnosis risk from demographics

Short and practical repository for the master's thesis: evaluate how well tabular foundation models and baselines predict diagnosis risk using demographic features from MIMIC‑IV.
With information Patients can provide in the waiting room.


# Table of Contents
- [Overview](#overview)

	- [Quick Facts](#quick-facts)

	- [Quick Start](#quick-start)

- [Main Tasks (Short)](#main-tasks-short)

- [Resources](#resources)

- [Notes](#notes)


## Overview

### Quick facts
- Goal: Measure predictive performance of foundation/tabular models (TabPFN, CatBoost, etc.) using only demographic features.
- Data: MIMIC‑IV (local CSVs in `files/…`) — original source: https://physionet.org/content/mimiciv/3.1/
- Notebook: `data_analysis.ipynb` — ingestion, DuckDB views and basic EDA are provided.

### Quick start
1. Install minimal deps in the notebook or environment:
	- `pip install -r requirements.txt` or in-notebook `!pip install duckdb polars pandas plotly`
2. Open `data_analysis.ipynb` and run the cells to create DuckDB views from CSVs (creates schema `ed`, `hosp`, `icu`).
3. Use read-only DuckDB for analysis when multiple sessions are active:
	- `duckdb.connect(database='mimic_v2.db', read_only=True)`

## Resources
- MIMIC docs: https://mimic.mit.edu/docs/
- TabPFN: https://github.com/PriorLabs/TabPFN

## Notes
- Use environment variables for secrets and avoid committing data files.
- For concurrent write workflows consider using PostgreSQL; DuckDB is single-writer.



