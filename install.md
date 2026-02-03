# Installation und Setup

Kurzanleitung, um das Projekt auf einer neuen Maschine lauffähig zu machen.

## Voraussetzungen
- Python >= 3.13 (getestet mit 3.13.3)
- Git
- macOS oder Linux (auf Windows via WSL empfohlen)

## Installation
1) Repository klonen
```bash
git clone <repo-url> fs-thesis
cd fs-thesis
```

2) Virtuelle Umgebung anlegen
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3) Abhängigkeiten installieren
- Schlank (nur Laufzeit):
```bash
pip install -e .
```
- Voll (inkl. Jupyter, Ruff, MkDocs):
```bash
pip install -e ".[dev]"
```
- Alternativ (ohne Extras):
```bash
pip install -r Archive/requirements.txt
```

## Daten einspielen
- Das Projekt erwartet die MIMIC-IV CSVs in `data/raw/` unter den vorhandenen Unterordnern (`ed/`, `hosp/`, `icu/`).
- Lege die originalen Dateien genau so ab, wie sie geliefert werden (keine Umbenennung). Prüfsummen findest du in den mitgelieferten `SHA256SUMS.txt`.

## Arbeiten mit Notebooks
Aktiviere die Umgebung und starte Jupyter Lab:
```bash
source .venv/bin/activate
jupyter lab
```

## Code-Qualität
Ruff ist konfiguriert:
```bash
ruff check .
ruff format .
```

## Dokumentation
MkDocs lokal starten:
```bash
mkdocs serve
```

## Tipps
- Falls `python` nicht 3.13 ist, verwende explizit `python3.13` oder passe den `PATH` an.
- Bei Paketproblemen: `pip install --upgrade pip setuptools wheel` und erneut installieren.
