# Thesis 
"How good is the performance of a foundation model to predict the risk of a diagnose, based on demographic data?" 

## Algorithm
https://github.com/PriorLabs/TabPFN

## Data
https://physionet.org/content/mimiciv/3.1/

## Literatur
https://www.frontiersin.org/journals/reproductive-health/articles/10.3389/frph.2021.756405/full

## To-Dos für Masterarbeit

### Datenvorbereitung
- [x] MIMIC-IV Zugang beantragen (PhysioNet Account + Training)
- [x] Daten herunterladen und in Projekt-Ordner laden
- [ ] Relevante Tabellen identifizieren (patients, admissions, diagnoses_icd)
- [ ] Explorative Datenanalyse: Demografische Verteilungen checken
- [ ] Missing Data analysieren und Strategie festlegen
- [ ] Train/Validation/Test Split definieren (zeitlich oder Patient-basiert)

### Feature Engineering
- [ ] Demografische Features definieren (Alter, Geschlecht, Ethnizität)
- [ ] Diagnose-Labels erstellen (ICD-10 Codes zu Risikogruppen mappen)
- [ ] Categorical Encoding (One-Hot, Label Encoding)
- [ ] Feature Scaling/Normalisierung implementieren

### Algorithmen & Modelle
- [ ] Baseline-Modelle implementieren: Logistische Regression, Random Forest
- [ ] Foundation Model auswählen: TabPFN, CatBoost, XGBoost
- [ ] LLM-basierte Ansätze testen (GPT mit Prompting)
- [ ] Deep Learning: TabNet, NODE, TabTransformer
- [ ] Ensemble-Methoden evaluieren

### Evaluation & Metriken
- [ ] Evaluation-Pipeline aufbauen (AUC-ROC, Precision, Recall, F1)
- [ ] Cross-Validation implementieren
- [ ] Calibration-Plots erstellen (Brier Score, Reliability Diagrams)
- [ ] Fairness-Metriken nach Subgruppen (Geschlecht, Alter, Ethnizität)
- [ ] Statistical Significance Tests zwischen Modellen

### Wichtige Überlegungen
- [ ] Class Imbalance Problem addressieren (SMOTE, Class Weights)
- [ ] Hyperparameter Tuning (Grid Search, Bayesian Optimization)
- [ ] Feature Importance Analyse (SHAP, Permutation Importance)
- [ ] Overfitting Detection (Learning Curves, Validation Curves)
- [ ] Computational Budget planen (GPU/CPU Ressourcen)

### Dokumentation & Reproduzierbarkeit
- [ ] requirements.txt oder environment.yml erstellen
- [ ] Seeds für Reproduzierbarkeit setzen
- [ ] Experiment-Tracking setup (MLflow, Weights & Biases)
- [ ] Code dokumentieren und strukturieren
- [ ] Results-Tabellen und Plots für Thesis erstellen

