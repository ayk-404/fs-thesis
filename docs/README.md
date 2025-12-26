# fs_thesis

**Master's Thesis: Predicting Diagnosis using Machine Learning**

A structured, reproducible research project developed to predict medical diagnoses. This project utilizes Python 3.13.3 and the Cookiecutter Data Science framework.

## 🚀 Getting Started

### Prerequisites

* **Python 3.13.3**
* **Homebrew** (for macOS dependency management)

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/fs-thesis.git
cd fs-thesis

```


2. **Set up the virtual environment:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```


3. **Install Dependencies:**
* **Core (Analysis Only):**
```bash
pip install -e .

```


* **Development (Jupyter, Ruff, MkDocs):**
```bash
pip install -e ".[dev]"

```





## 📁 Project Structure

```text
├── LICENSE
├── README.md          <- Project overview and setup instructions.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate transformed data.
│   ├── processed      <- Final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
├── docs               <- Project documentation (MkDocs).
├── fs_thesis          <- Source code for use in this project.
│   ├── __init__.py    <- Makes fs_thesis a Python module.
│   └── features       <- Scripts to turn raw data into features.
├── models             <- Trained and serialized models.
├── notebooks          <- Jupyter notebooks for exploration and analysis.
└── pyproject.toml     <- Configuration for dependencies and build tools.

```

## 🛠 Development Workflow

### Jupyter Notebooks

To start the research environment and access notebooks:

```bash
jupyter lab

```

### Code Quality (Linting & Formatting)

We use **Ruff** for maintaining high code standards. It is configured in `pyproject.toml`.

```bash
ruff check .    # Identify errors or linting issues
ruff format .   # Automatically fix formatting to PEP8

```

### Documentation

Project documentation is managed via **MkDocs**.

* **Preview locally:** `mkdocs serve`
* **Generate site:** `mkdocs build`

## 📊 Data Management

**Note:** The `data/` and `models/` directories are ignored by Git to prevent large files from being tracked.

* Ensure raw data is placed in `data/raw/` before running notebooks.
* Use the provided scripts in `fs_thesis/` to process data from `raw` to `processed`.

## 📝 Author

* **Andrey Kudryavtsev** — Master's Candidate

## 📜 License

## This project is licensed under the MIT License - see the [LICENSE](https://www.google.com/search?q=LICENSE) file for details.
