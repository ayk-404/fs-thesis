# ToDo

## 🔴 Prio 1 — Thesis-Kern

- [ ] **Benchmark-Notebook** erstellen (`models/Benchmark.ipynb`)
    - [ ] DummyClassifier (Baseline)
    - [ ] LogisticRegression
    - [ ] RandomForest
    - [ ] XGBoost
    - [ ] TabPFN (gleiche Pipeline wie v4)
    - [ ] Vergleichstabelle: AUC, F1, Accuracy, per-class F1
- [ ] **Data Quality Check**: Gestorbene Patienten als "gesund" (target=2) klassifiziert? → `dod` prüfen
- [ ] **Feature Ablation**: Modell nur mit age+bmi vs. alle 8 Features → zeigt ob Rest nur Rauschen
- [ ] **Thesis schreiben**: Fokus auf Interpretation: "Warum sind demographische Daten Prädiktoren?"

## 🟡 Prio 2 — Vertiefung

- [ ] SHAP nutzen (https://www.aidancooper.co.uk/a-non-technical-guide-to-interpreting-shap-analyses/)
- [ ] Evaluierung & Bias-Check: Vorhersage schlechter für bestimmte Ethnizitäten/Versicherungsklassen?
- [ ] Ergebnisse (Reports) hochladen in git
- [ ] Interaktionseffekte anschauen (https://www.statology.org/how-to-spot-interaction-effects-using-python-plots/)

## 🟢 Prio 3 — Nice-to-have

- [ ] Verallgemeinerung: nicht nur Herzfehler, sondern auch andere Diagnosen
- [ ] Cross-Validation recherchieren und ggf. einbauen
- [ ] mkdocs einpflegen (https://www.youtube.com/watch?v=DeZjkCtttss)
- [ ] update LICENSE

## ✅ Erledigt

<details><summary>Abgeschlossene Aufgaben</summary>

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
