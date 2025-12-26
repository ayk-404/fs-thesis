# fs-thesis: Diagnosis Prediction

## Project Overview

**fs-thesis** is a Master's thesis project focused on predicting diagnoses. It utilizes a modern Data Science stack to process medical data (MIMIC dataset), employing DuckDB for efficient data storage/querying and Polars/Pandas for analysis and modeling.

### Tech Stack
*   **Language:** Python (>= 3.13)
*   **Database:** DuckDB (`data/mimic_v2.db`)
*   **Data Processing:** Polars, Pandas, NumPy
*   **Modeling:** Scikit-learn
*   **Visualization:** Plotly, Matplotlib
*   **Tools:** Ruff (linting), Make (automation)

### Architecture
The data pipeline follows a clear path:
1.  **Raw Data:** CSV files stored in `data/raw/{ed,hosp,icu}/`.
2.  **Database:** `fs_thesis/create_views.py` creates views in a local DuckDB instance (`data/mimic_v2.db`) pointing to these raw CSVs.
3.  **Analysis:** Jupyter notebooks in `notebooks/` query the database using helper functions in `fs_thesis/helper.py`.
4.  **Modeling:** Scikit-learn models are trained on the processed data.

## Getting Started

### 1. Installation
The project uses `pyproject.toml` for dependency management.
*   **Install dependencies:**
    ```bash
    pip install -e .
    # OR
    pip install -e ".[dev]"  # for development tools like ruff, jupyter
    ```
    *Note: The `Makefile` references a `requirements.txt` which may be missing or located in `Archive/`. Prefer `pip install -e .`.*

### 2. Data Setup
Initialize the DuckDB database by creating views for the raw CSV files.
```bash
python fs_thesis/create_views.py
```
This script scans `data/raw` and updates `data/mimic_v2.db`.

### 3. Running Notebooks
Start the Jupyter server:
```bash
jupyter lab
```
Notebooks are located in `notebooks/`.

## Development Workflow

### Key Commands (Makefile)
*   **Linting:** `make lint` (runs `ruff check`)
*   **Formatting:** `make format` (runs `ruff format`)
*   **Testing:** `make test` (runs `unittest`)
    *   *Warning: The current test suite (`tests/test_data.py`) contains a placeholder failing test.*
*   **Clean:** `make clean` (removes pycache)

### Coding Conventions
*   **Style:** Adhere to PEP 8. The project uses `ruff` for strict linting and formatting.
*   **Data Access:**
    *   Use `fs_thesis.helper.sql(query)` to execute SQL against the DuckDB instance.
    *   This function returns a **Polars DataFrame**.
    *   Use `fs_thesis.helper.show(df)` to display DataFrames in notebooks.
*   **Paths:** Use `pathlib` or `os.path` relative to the repository root.

## Key Files & Directories

*   `fs_thesis/`
    *   `helper.py`: Contains `sql()` and `show()` utilities for database interaction.
    *   `create_views.py`: ETL script to set up the DuckDB environment.
*   `data/`: Stores raw and processed data.
    *   `mimic_v2.db`: The main DuckDB database file.
*   `notebooks/`: Analysis and experimentation.
    *   `regression.ipynb`, `diagnoses.ipynb`: Core analysis notebooks.
*   `pyproject.toml`: Configuration for dependencies and tools (Ruff).
*   `Makefile`: Automation for common tasks.
