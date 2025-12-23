# fs-thesis documentation!

## Description

master thesis to predict diagnosis

## Commands

The Makefile contains the central entry points for common tasks related to this project.

> **Info**   
> starte mit stupiden algo und werde nach und nach komplexer

# to-dos
#### data understanding
- [x] Diagnose kategorisieren für welche man Daten hat
- [x] erster Scatter Plot
- [ ] remove unnessecary files and code
- [ ] clean up the code in the notebooks  
#### data preprocessing
- [ ] Encode the data (One-Hot-Encoder), to fit it into a PCA (Principal Component Analysis) -> Curse of D.
- [ ] Scatter Analyse von Datenpunkten und ihrer Verteilung (PC1 & PC2)
- [ ] Korrelation analysieren, obs eine Korrelation gibt und wenn ja welche? 
- [ ] Regression ausprobieren
    - [ ] lineare Regression kurze Recherche
    - [ ] logistische Regression kurze Recherche


### Main tasks (short)
- Data prep: load CSVs, create DuckDB views/tables, harmonize schemas.
- Feature engineering: demographic features, label mapping from ICD codes.
- Models: baselines (logistic regression, random forest), TabPFN, tree-based models, LLM experiments.
- Evaluation: AUC, F1, calibration, subgroup fairness analyses.

- [ ] Interaktionseffekte untersuchen

# Optional / Ideen
- [ ] Datenset erweitern mit zb BMI? (Macht das Sinn?)

# Abuse and Dependence
Thesis patients with abuse or dependence have a higher risk for certain diagnosis than patients without. To have a narrow scope I choose the 5 common drugs according to the NIDA. 
Beside the substances depression will be also included. During the last years there is an incresing trend in the US. (western world). There are several papers on depression and its effects on the health.

https://nida.nih.gov/sites/default/files/cadchart.pdf

| Substance | ICD Code / Identifier | Description |
|---|---|---|
| Nicotine | `172,10` | Nicotine dependence |
| Alcohol | `F101,10` | Alcohol abuse |
| Alcohol | `F102,10` | Alcohol dependence |
| Opioids | `30550,9` | Opioid abuse, unspecified |
| Opioids | `F112,10` | Opioid dependence |
| Cannabis | `F121,10` | Cannabis abuse |
| Cannabis | `F122,10` | Cannabis dependence |
| Cocaine | `F141,10` | Cocaine abuse |
| Cocaine | `F142,10` | Cocaine dependence |
| Depression | `F32A,10` | Depression unspecified |


