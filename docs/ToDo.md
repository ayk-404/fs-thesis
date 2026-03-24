# ToDo

## 🔴 Prio 1 — Thesis-Kern

- [x] TabICL vergleichen
- [x] Beantworten, warum TabPFN langsamer ist (präzise beantworten)
- [x] recall: echt positiv (positiv identifizierte) (30% von 100% - die krank sind) mit in Thesis aufschreiben
- [x] precision: von allen die krank sind wie viele sind wirklich krank (baysan precision) in Thesis aufschreiben
- [x] TabPFN mit einem Loop ist verlgeichbar, weil Robust - mit Beweis in Thesis aufnehmen
- [x] XGB trainieren
- [x] Gliederung schreiben (Arbeit von Innen nach Aussen schreiben, Ergebinsse dann Einleitung etc.)
- [x] Paper zu TabPFN tune lesen
- [x] Entscheiden ob tune gemacht wird und das ggf ausführen
- [x] Im Paper Entscheidung dokumentieren (Gliederung)
- [x] Struktur der Arbeit Generel -> Detail -> Generel (in Gliederung mit aufnehmen & 4.1 recall und precision erklären)
- [ ] Punkt 6.3 überdenken (always end on a high note): Fundamental, tiefreichende Stoßrichtung - was das Highlight ist
- [ ] TItel bestimmen
- [ ] schreiben Kap 3 (Zugänglich machen für Punch lines in 4 und 5)
- [ ] schreiben Kap 4
- [ ] schreiben Kap 2
- [ ] schreiben Kap 5
- [ ] schreiben Kap 6
- [ ] schreiben Kap 1

## 🟡 Prio 2 — Vertiefung

- [ ] SHAP nutzen (https://www.aidancooper.co.uk/a-non-technical-guide-to-interpreting-shap-analyses/)
- [ ] Evaluierung & Bias-Check: Vorhersage schlechter für bestimmte Ethnizitäten/Versicherungsklassen?
- [x] Ergebnisse (Reports) hochladen in git
- [ ] Interaktionseffekte anschauen (https://www.statology.org/how-to-spot-interaction-effects-using-python-plots/)

## 🟢 Prio 3 — Nice-to-have

- [ ] Cross-Validation recherchieren und ggf. einbauen (kein Sinn bei TabPFN, da kein Training)
- [ ] mkdocs einpflegen (https://www.youtube.com/watch?v=DeZjkCtttss)
- [ ] update LICENSE

## ✅ Erledigt

<details><summary>Abgeschlossene Aufgaben</summary>
- [x] **Benchmark-Notebook** erstellen (`models/Benchmark.ipynb`)
    - [x] DummyClassifier (Baseline)
    - [x] LogisticRegression
    - [x] RandomForest
    - [x] XGBoost
    - [x] TabPFN (gleiche Pipeline wie v4)
    - [x] Vergleichstabelle: AUC, F1, Accuracy, per-class F1
- [x] **Data Quality Check**: Gestorbene Patienten als "gesund" (target=2) klassifiziert? → `dod` prüfen
- [x] load csv files into duck.db
- [x] SQL-Extraktion (demographische Daten + Time-to-Event)
- [x] BMI implementieren als Feature
- [x] Datenbereinigung & Preprocessing
- [x] Features aufschlüsseln (Risk-Analyse pro Subgruppe)
- [x] Robustheit bestätigen (20 Runs, n_samples=300)
- [x] ROC-AUC Analyse + Visualisierung
- [x] Loop aufbauen (Checkpoints, Logging, Config-Vergleich)
- [x] Feature Importance (Permutation, n_repeats=10, f1_macro)
- [x] Confusion Matrix + Sankey
- [x] TabPFN auf MPS (Apple Metal) optimiert
- [x] Code modular aufgebaut (data_loader.py, preprocessing.py)
- [x] Notebook-Struktur finalisiert (TabPFN_v4)

</details>
