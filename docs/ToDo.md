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
#### Fahrplan
- [x] SQL-Extraktion. Erstelle eine Tabelle, die für jeden Patienten die demographischen Daten und die "Time-to-Event" (Tage bis ICD-Code X) enthält.
- [x] Code von SQL-Extraction dokumentieren
- [x] Lizenz von Huggingface holen und tabpfn implementieren https://docs.priorlabs.ai/how-to-access-gated-models
- [x] nächste Schritte von Chatty machen
- [x] Datenbereinigung & Preprocessing. Behandle fehlende Werte (Imputation) und kodiere kategoriale Daten für die Baselines (TabPFN braucht das oft nicht!).
- [x] kg, Height oder BMI implementieren als Feature
- [x] Features aufschlüsseln
- [x] logs einbauen
- [x] Robustheit bestätigen/prfen mit 30 durchläufen mit 300 samples
- [x] Man könnte die Features aufteilen also welche Art von Insurance, welche gender (m oder w), etc um mehr Analysewerte "Verständnis" zu bekommen.
- [x] Encode the data (One-Hot-Encoder), to fit it into a PCA (Principal Component Analysis) -> Curse of D.
- [x] TabPFN auf msp und 9000 balanced sample prüfen statt cpu und kline sample (bwz vielleicht beides und dann verlgeichen)
- [x] manuell code durchgehen und optimieren
- [x] daten modular aufbauen
- [ ] Ergebnisse (Reports) hochladen in git
- [ ] Loop aufbauen in TabPFN (Training speichern, Gesamt-Analyse)
- [ ] roc-auc analyse einbauen
- [ ] logs validieren in einer guten darstellung (avg, mittelwert, varianz)
- [ ] baseline aufbauen (Multinomiale Logistische Regression): Gemini Chat.
- [ ] benchmark aufbauen
    - [ ] xgboost, random forest, TabPFN, LLM experiments (Lesen welche Model am besten passen könnte mit Begründung)
- [ ] Vergleich der Algos mithilfe von AUC, F1, calibration, subgroup fairness analyses
- [ ] checken ob der patient als gestorben trz "gesund" ist

### Recherche
- [ ] Tutorial machen für Algos
- [ ] SHAP nutzen https://www.aidancooper.co.uk/a-non-technical-guide-to-interpreting-shap-analyses/
- [ ] recherche "was ist Cross-Validation" anschauen.
- [ ] Evaluierung & Bias-Check. Analysiere: Vorhersagt das Modell für bestimmte Ethnizitäten oder Versicherungsklassen schlechter? (Wichtig für den "aktuellen" Teil der Arbeit).

#### post work
- [ ] Thesis schreiben. Fokus auf die Interpretation: "Warum sind demographische Daten Prädiktoren für die Zeitspanne bis zur Krankheit?"
- [ ] update LICENSE
- [ ] mkdocs einpflegen https://www.youtube.com/watch?v=DeZjkCtttss
- [ ] Interaktionseffekte anschauen (https://www.statology.org/how-to-spot-interaction-effects-using-python-plots/)

### i-tüpfelchen
- [ ] Veralgemeinerung nicht nur Herzfehler, sondern auch andere Diagnosen.
- [ ] negatives feature verschlechtert das modell. auswerten welches immer negativ ist und dass mal weglassen danaach vergleichen mit anderen durchgängen
