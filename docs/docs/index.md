# fs-thesis documentation!

## Description

master thesis to predict diagnosis

## Commands

The Makefile contains the central entry points for common tasks related to this project.

> **Info**   
> starte mit stupiden algo und werde nach und nach komplexer
<details open>
    <summary># To-Do's</summary>

    # to-dos
    #### data prep
    - [x] load csv files into duck.db
    #### data EDA
    - [x] Diagnose kategorisieren für welche man Daten hat
    - [x] erster Scatter Plot
    - [x] remove unnessecary files and code
    - [x] clean up the code in the notebooks 
    #### data preprocessing
    - [ ] Encode the data (One-Hot-Encoder), to fit it into a PCA (Principal Component Analysis) -> Curse of D.
    - [ ] Interaktionseffekte untersuchen
    - [ ] Scatter Analyse von Datenpunkten und ihrer Verteilung (PC1 & PC2)
    - [ ] Korrelation analysieren, obs eine Korrelation gibt und wenn ja welche? 
    - [ ] Regression ausprobieren
        - [ ] lineare Regression kurze Recherche
        - [ ] logistische Regression kurze Recherche
    #### model work
    - [ ] random forest, TabPFN, LLM experiments (Lesen welche Model am besten passen könnte mit Begründung)
    - [ ] Evaluation mithilfe von AUC, F1, calibration, subgroup fairness analyses
    #### post work
    - [ ] update LICENSE
</details>

# Optional / Ideen
- [ ] Datenset erweitern mit zb BMI? (Macht das Sinn?)
- [ ] GUI for entry data and app for patients

# Tipps
Oliver: Fasse die Aufenthalte zusammen, damit das aussagekräftiger wird. Und man sagen kann was zb Marta bekommt.  

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


