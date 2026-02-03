# ToDo
#### data prep
- [x] load csv files into duck.db
#### data EDA
- [x] Diagnose kategorisieren für welche man Daten hat
- [x] erster Scatter Plot
- [x] remove unnessecary files and code
- [x] clean up the code in the notebooks 
#### data preprocessing
- [x] make a one-hot-encode tutorial
- [x] make a PCA tutorial
- [x] find the right data to predict a certain illness (infection)
#### Gemini Fahrplan (https://gemini.google.com/app/7616ffc8ea6a56f7)
- [x] SQL-Extraktion. Erstelle eine Tabelle, die für jeden Patienten die demographischen Daten und die "Time-to-Event" (Tage bis ICD-Code X) enthält.
- [x] Code von SQL-Extraction dokumentieren
- [x] Lizenz von Huggingface holen und tabpfn implementieren https://docs.priorlabs.ai/how-to-access-gated-models
- [x] nächste Schritte von Chatty machen
- [x] Datenbereinigung & Preprocessing. Behandle fehlende Werte (Imputation) und kodiere kategoriale Daten für die Baselines (TabPFN braucht das oft nicht!).
- [ ] kg, Height oder BMI implementieren als Feature
- [ ] logs einbauen
- [ ] Robustheit bestätigen/prfen mit 30 durchläufen mit 300 samples
- [ ] logs validieren in einer guten darstellung (avg, mittelwert, varianz)
- [ ] 10k durchlauf machen als referenz
- [ ] Man könnte die Features aufteilen also welche Art von Insurance, welche gender (m oder w), etc um mehr Analysewerte "Verständnis" zu bekommen.
- [ ] recherche "was ist Cross-Validation" anschauen.
- [ ] Evaluierung & Bias-Check. Analysiere: Vorhersagt das Modell für bestimmte Ethnizitäten oder Versicherungsklassen schlechter? (Wichtig für den "aktuellen" Teil der Arbeit).
- [ ] Thesis schreiben. Fokus auf die Interpretation: "Warum sind demographische Daten Prädiktoren für die Zeitspanne bis zur Krankheit?"

- [ ] Interaktionseffekte anschauen (https://www.statology.org/how-to-spot-interaction-effects-using-python-plots/)
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
- [ ] mkdocs einpflegen https://www.youtube.com/watch?v=DeZjkCtttss

### i-tüpfelchen
- [ ] Veralgemeinerung nicht nur Herzfehler, sondern auch andere Diagnosen.
