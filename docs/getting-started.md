# Getting Started

This guide describes how to set up the project environment, initialize the data, and run the analysis.

## Prerequisites

- **Python:** Version 3.13 or higher is required.
- **Data:** Access to MIMIC-IV dataset (CSV files placed in `data/raw/`).

## Installation

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone https://github.com/ayk-404/fs-thesis
    cd fs-thesis
    ```

2.  **Install dependencies:**
    The project uses `pyproject.toml` for dependency management.
    ```bash
    pip install -e .
    # For development tools (notebooks, linting):
    pip install -e ".[dev]"
    ```

## Data Setup

The project uses a local DuckDB database (`data/mimic_v2.db`) which interfaces with raw CSV files. The CSV files for this database are from physionet.org.  

1.  **Prepare Raw Data:**
    Ensure your MIMIC-IV CSV files are organized in `data/raw/` under subdirectories `ed`, `hosp`, and `icu`.

2.  **Initialize Database Views:**
    Run the setup script to create the necessary views in DuckDB:
    ```bash
    python fs_thesis/create_views.py
    ```
    This will scan the `data/raw` directories and update the database schema.

## Running Analysis

1.  **Start Jupyter Lab:**
    ```bash
    jupyter lab
    ```

2.  **Open Notebooks:**
    Navigate to the `notebooks/` directory to find analysis files like `diagnoses.ipynb` or `regression.ipynb`.

## Important Notes

- **DuckDB Concurrency:** DuckDB is single-writer. If you need to run multiple concurrent write operations, consider using PostgreSQL. For analysis (read-only), you can connect multiple sessions:
    ```python
    import duckdb
    con = duckdb.connect(database='../data/mimic_v2.db', read_only=True)
    ```
- **Secrets:** Use environment variables for sensitive information. Do not commit data files to the repository.