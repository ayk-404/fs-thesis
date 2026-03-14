 ## 14.03.2026
 Die bisherigen Modelle haben ihre default werte hinterlegt, kein Training (keine Spezialisierung).

 Robustness Loop shows the variance. So the models are performing stable.
 The tuned versions, shows what the models could achieve. 
 ### honest limitation to acknowledge
 All F1 Macro values are low (0.36–0.40). The reason is your class distribution:
Early:   1,719  (~4.8%)
Late:    1,304  (~3.6%)
Healthy: 32,730 (~91.5%)
No model can do well on Early and Late when they represent less than 5% of the data each. The F1 for class 2 (Healthy) is likely ~0.95+ for every model — but that gets averaged with the poor minority class scores, pulling F1 Macro down. This is not a model failure — it is a data reality that needs to be stated clearly in your thesis.

 ### Balancing data for tuned models
 the models will train on the whole data. So its important to handle the balancing.
### One Quote for the thesis:
 TabPFN matches classical models in the small-data regime and achieves superior probability calibration (AUC), but fully-trained RF and XGBoost outperform it on F1 Macro — suggesting TabPFN's zero-shot advantage is most valuable when labeled data is scarce.

Methods — Hyperparameter Optimization Strategy

To obtain well-tuned classical baselines, Random Forest and XGBoost were trained using a two-stage procedure. First, hyperparameters were optimized via RandomizedSearchCV with 30 candidates and 3-fold cross-validation on a stratified subsample of 20,000 training examples. This subsample-based search was chosen to maintain a feasible runtime while covering a broad hyperparameter space. The best configuration was subsequently used to refit each model on the full training set of 143,008 examples, yielding the final RF_tuned and XGB_tuned baselines.


Results/Discussion — Interpretation of the Tuned Models

The XGBoost training history (Figure X) shows train and validation loss converging in parallel across all 200 boosting rounds, with no sign of overfitting. Notably, the best validation round coincides with the final round (round 199), suggesting that performance had not yet fully plateaued and that additional estimators could yield marginal further gains.
A gap is observable between the cross-validation F1 of the best HPO candidate (0.43, measured on 20k rows) and the final validation F1 after refit on the full training set (0.394). This discrepancy reflects a known limitation of subsample-based HPO: hyperparameters optimized on a smaller distribution do not transfer perfectly to a larger, more heterogeneous training set. This gap is not indicative of overfitting, but rather of the approximation inherent in the chosen HPO strategy. Given the scope of this thesis, full-data HPO was deemed computationally infeasible; the resulting baselines nonetheless represent a substantially stronger upper bound than the 300-sample regime used for the robustness benchmark.

 ## 09.03.2026
 TabPFN hat per Design kein echtes Training — 20 Loops mit verschiedenen Trainingssamples gibt dir Varianz-Information, aber der Mehrwert gegenüber 1 Run ist begrenzt. Bei sklearn-Modellen macht es mehr Sinn weil die stärker vom Trainingsset abhängen.
 
 ## 04.03.2026

### Gender-Paradoxon bestätigt sich in den Plots

Im Plot "Risk by Gender and Insurance" haben Männer einen klar höheren durchschnittlichen Risiko-Score. Gleichzeitig zeigt die Feature Importance für Gender einen **negativen Wert** — das Modell wird also besser wenn man Gender zerstört (shuffelt).

Das ist kein Widerspruch:
- **Risk by Gender (Bar Chart):** Deskriptive Statistik. Männer sind im Schnitt kränker → höherer Score. Aber das liegt an Confoundern (Alter, BMI, Insurance-Verteilung), nicht am Geschlecht selbst.
- **Feature Importance (Permutation):** Kausale Analyse. Gender bringt keine *eigene* Vorhersagekraft wenn Age und BMI schon bekannt sind. Im Gegenteil, es erzeugt Rauschen → negativer Importance-Wert = Feature schadet dem Modell.

Das bestätigt die Beobachtung vom 10.02. (Gender-Paradoxon). Das Modell erkennt Scheinkorrelationen und ignoriert Gender zugunsten der echten Treiber. Für die Thesis ist das ein Argument für Robustheit gegen Confounding.

### Gender-Paradoxon bestätigt sich in den Plots

Im Plot "Risk by Gender and Insurance" haben Männer einen klar höheren durchschnittlichen Risiko-Score. Gleichzeitig zeigt die Feature Importance für Gender einen **negativen Wert** — das Modell wird also besser wenn man Gender zerstört (shuffelt).

Das ist kein Widerspruch:
- **Risk by Gender (Bar Chart):** Deskriptive Statistik. Männer sind im Schnitt kränker → höherer Score. Aber das liegt an Confoundern (Alter, BMI, Insurance-Verteilung), nicht am Geschlecht selbst.
- **Feature Importance (Permutation):** Kausale Analyse. Gender bringt keine *eigene* Vorhersagekraft wenn Age und BMI schon bekannt sind. Im Gegenteil, es erzeugt Rauschen → negativer Importance-Wert = Feature schadet dem Modell.

Das bestätigt die Beobachtung vom 10.02. (Gender-Paradoxon). Das Modell erkennt Scheinkorrelationen und ignoriert Gender zugunsten der echten Treiber. Für die Thesis ist das ein Argument für Robustheit gegen Confounding.

### Confounding-Muster: Nicht nur Gender, auch Insurance

Das selbe Muster wie beim Gender-Paradoxon zeigt sich bei Insurance. Medicare-Patienten haben im Bar Chart den höchsten Risiko-Score — aber Medicare bekommt man in den USA ab 65 Jahren. Der hohe Score kommt also nicht von der Versicherungsart, sondern weil Medicare-Patienten **alt** sind. Insurance kodiert Alter nochmal redundant.

Wenn das Modell `anchor_age` schon kennt, bringt `insurance` keine neue Information. Das gleiche gilt vermutlich auch für `race` und `marital_status`. Damit bleiben von 8 Features nur **2 echte Treiber**: `anchor_age` und `bmi`. Der Rest sind Proxies oder Rauschen.

Das ist kein Versagen des Modells — im Gegenteil: Das Modell entlarvt **systematisch** Scheinkorrelationen in den demografischen Daten. Drei Features (Gender, Insurance, möglicherweise Race) zeigen deskriptiv klare Unterschiede, aber das Modell erkennt dass die Unterschiede nicht von diesen Features kommen, sondern von Alter und BMI dahinter.

### Fazit: Screening ja, Diagnose nein

Demografische Daten reichen nicht für eine klinische Diagnose, aber für ein **vorgelagertes Screening**. Das Modell identifiziert Risikopatienten basierend auf Daten die ohne zusätzlichen Aufwand bei jeder Aufnahme existieren — ohne Labor, ohne EKG, ohne Bildgebung.

Es ersetzt keine Diagnostik, sondern priorisiert den Zugang dazu. Das passt zur Thesis-Argumentation vom 16.02.:
- **Barrierefreiheit:** Nur patientenzentrierte Daten, keine klinische Infrastruktur nötig.
- **Ressourceneffizienz:** Triage-System, das Hochrisikopatienten gezielt zur Diagnostik leitet.
- **Limitation ehrlich benennen:** F1 zeigt die Grenzen der Vorhersagegenauigkeit, AUC zeigt dass eine Trennschärfe da ist.

### Notebook-Struktur: Finale Reihenfolge

Test (Section 6.2) kommt vor Feature Importance (Section 7) weil `clf_best` in der Test-Zelle erstellt wird. Methodisch sind die beiden Analysen unabhängig voneinander — `clf_best` verändert sich nicht durch predict oder permutation. Die Reihenfolge ist rein technisch bedingt (Code-Abhängigkeit).

### Feature Importance: Warum X_val und nicht X_test?

Feature Importance wird auf `X_val` berechnet, nicht auf `X_test`. Das Test-Set wird in Section 6.2 einmalig für die finale Metrik angefasst. Wenn man es ein zweites Mal für Feature Importance nutzt, "lernt" man etwas über das Test-Set → die Test-Metriken wären nicht mehr unbiased. Das Val-Set wurde nie zum Trainieren verwendet, also misst die Permutation den echten Einfluss auf ungesehene Daten — ohne das Test-Set zu kontaminieren.



## 03.03.2026

### Notebook-Refactoring: TabPFN_v3 (Final Structure)

Das Notebook wurde komplett aufgeräumt. Tote Zellen (alter `classifier` auf Test-Samples) wurden entfernt. Die finale Struktur sieht so aus:

```
1.  Data Pipeline
2.  Preprocessing (Split + Balance)
3.  Training Quick-Check (classifier)
4.  Validation Quick-Check (1000 Samples)
5.  Visualization (BMI, Age, Insurance, Confusion Matrix, Sankey)
6.  Robustness Loop (3 Configs × 20 Runs)       ← Hauptergebnis
6.1 Robustness Viz (Bar + Violin)
7.  Test (clf_best auf Test-Set)                 ← Bestätigung
8.  Feature Importance (clf_best, n_repeats=10)  ← Erklärung
```

Sections 3-5 sind der schnelle Sanity-Check. Sections 6-8 sind die Thesis-Ergebnisse.

### Robustness Loop: 3 Ensemble-Configs

Es werden 3 Konfigurationen verglichen (`n_estimators`: 8, 32, 64) über je 20 Runs mit verschiedenen Seeds. Das Balancing wird pro Run neu gezogen (`balance_data(seed=42+i)`), das Val-Set bleibt fix (Ceteris paribus, wie gehabt).

### Test-Evaluation: Bestes Modell aus dem Loop

Nach dem Loop wird der Run mit dem höchsten F1-Macro identifiziert. Das Modell wird mit dem gleichen Seed reproduziert (`clf_best`) und einmalig auf dem **Test-Set** evaluiert (nicht Val!). Damit ist die Trennung sauber: Val für Optimierung, Test für finale Aussage.

### Design-Entscheidung: Feature Importance als Einzelaufruf (nicht im Loop)

**Entscheidung:** Feature Importance wird einmalig mit `clf_best` auf dem vollen `X_val` berechnet (`n_repeats=10`), nicht im Robustness Loop.

**Begründung:**
- `permutation_importance` shuffelt intern 10× pro Feature → man bekommt `mean ± std` aus einem Aufruf. Das ist methodisch solide.
- Die Varianz entsteht durch das Shuffeln der Features auf `X_val`, nicht durch verschiedene Modelle. `X_val` ist in allen Szenarien identisch (gleiches Set, gleiche Verteilung).
- Ein einzelner Run mit `n_repeats=10` = 10 Messpunkte pro Feature. Das reicht für stabile Error Bars.
- Im Loop hätte man 20 Modelle × 5 Repeats = 100 predict-Aufrufe **extra**. Bei ~3min pro Predict wären das ~5h zusätzliche Laufzeit für einen marginalen Gewinn.
- **Scoring:** `f1_macro` statt default (accuracy), passend zur Hauptmetrik der Thesis.

> **Warum kein Bias durch einzelnes Modell?**
> Die Sorge wäre: Was wenn `clf_best` zufällig eine andere Feature-Gewichtung hat als der Durchschnitt?
> Das ist bei 8 Features und einem stabilen Val-Set extrem unwahrscheinlich. Die Permutation misst den Einfluss auf die Vorhersage von `X_val` — und `X_val` ändert sich nie. Wenn Age im besten Modell wichtig ist, ist es auch in den anderen wichtig, weil die Datenverteilung identisch ist.

### Notebook-Hygiene
- `skip`-Toggle durch Guard ersetzt: `if 'clf_best' not in dir()` → Feature Importance wird automatisch übersprungen wenn der Loop noch nicht gelaufen ist. Kein manuelles Umschalten mehr nötig.
- Alte Test-Zellen mit `classifier.predict(X_test_sample)` gelöscht (redundant, nutzte altes Modell auf nur 1000 Samples).
- Run-Ordner mit Timestamp, Checkpoints nach jeder Config, Log-File für Overnight-Runs.

## 01.03.2026
`reports/robustness_metrics_2026-03-01_17-50-30.csv`
Die Auswertung anhand von F1 zeigt, dass das Model zwar stabil ist, aber noch zu ungenau errät (F-1 Score).
Ich gebe recall und precision aus. Somit kann ich festlegen woher die niedrige prozentzahl kommt trotz gutem Ergebnis.  
`reports/robustness_metrics_2026-03-01_17-50-30.csv`  
In den neuen Ergebnissen sieht man precision und recall im Vergleich zum F1 (alle Werte in Macro = AVG).
Das Balancing in der balance_data funktion wurde angepasst, damit ein undersampling und oversampling eine ausgewogene Mitte findet.  
Trainings Iterationen werden auf 30 erhöht.

## 22.02.2026
Beobachtung. TabPFn ist effizienter als gleiche Algos (ref. TabPFn Paper p.322). Es ergibt sich daraus eine Machbarkeit und leichtere Anwendung für Cross-Use Cases.  
Sollte in meiner Thesis, wie erwartet TabPFN am besten abscheiden. So bestätigt sich die Aussage aus dem Paper p.323.
Mein Fazit in der Thesis sollte auf die Anwendbarkeit und Machbarkeit rauslaufen.

## 16.02.2026

### Methodik & Modell-Verständnis

**F1-Score vs. ROC-AUC**
*   **Erkenntnis:** Der F1-Score misst die Balance zwischen Sicherheit und Fehlalarmen, während ROC-AUC bewertet, wie gut ein Algorithmus das Krankheitsbild grundsätzlich im Vergleich zu einem anderen versteht (Trennschärfe).
*   **Kontext der Thesis:**
    *   **Recall (Sensitivität) als Priorität:** Bei Herzinsuffizienz darf kein Kranker übersehen werden (False Negative wiegt schwerer als False Positive).
    *   **ROC-AUC:** Belegt die ausreichende Trennschärfe des "Patienten-Modells" (nur anamnestische/demografische Daten) im Vergleich zu klinischen Modellen.
    *   **F1-Score:** Zeigt die Balance, um eine Flut an Fehlalarmen zu vermeiden (Gesunde fälschlich als krank klassifiziert).

**Wissenschaftliche Begründung (Argumentation)**
*   **Barrierefreiheit:** Fokus auf Patient-Reported Outcomes (Anamnese, Demografie) senkt die Hürde für frühe Risikoeinschätzung.
*   **Ressourceneffizienz:** Fungiert als Triage-System, um Hochrisikopatienten gezielt zur Diagnostik zu leiten.
*   **Klinische Plausibilität (SHAP):** Widerlegt den "Alte-Leute-Bias". SHAP zeigt, dass nicht das Alter allein, sondern die Kombination (z.B. mit BMI, Rauchstatus) entscheidend ist.

**Projekt-Fortschritt: Modularisierung**
Das Notebook `TabPFN_v2` wurde modular für Daten und Preprocessing umgebaut, um die Wiederverwendbarkeit des Codes zu gewährleisten.

### Besonderheiten an TabPFN (Hintergrund)

1.  **Kein klassisches Training:** Keine Gradientenoptimierung (Backpropagation); die Gewichte ändern sich nicht.
2.  **Transformer-Architektur:** TabPFN betrachtet den gesamten Trainingsdatensatz (Features + Labels) als einen "Prompt" (ähnlich GPT). Es nutzt Self-Attention-Mechanismen, um Beziehungen im Single Forward Pass zu verstehen.
3.  **Approximierte Bayes-Inferenz:** Berechnung der posterioren prädiktiven Verteilung: $P(y_{test} | x_{test}, D)$.

### Neue These
> Entwicklung eines schwellenwertoptimierten Screening-Verfahrens zur Prädiktion von Herzinsuffizienz auf Basis patientenzentrierter Merkmale unter Verwendung von Tabular Posterior Sampling (TabPFN).


## 11.02.2026
**Robustness & Visualisierung (Master-Thesis Level)**

1.  **Experiment-Design:**
    -   **Fixes Validierungs-Set:** Wir variieren nur das Training (30 Runs), nicht das Test-Set. Nur so messen wir echte Modell-Varianz ("Ceteris paribus").
    -   **Loop-Update:** Speicherung der Risk-Scores pro Subgruppe (z.B. `risk_bmi_obese`) in der CSV, um nicht nur *dass* ein Feature wichtig ist zu messen, sondern auch *in welche Richtung* es wirkt (medizinischer Plausibilitäts-Check).

2.  **Visualisierung:**
    -   **Bar-Charts mit Error-Bars:** Standard für wissenschaftliche Arbeiten (Mean ± StdDev). Ersetzt reine Boxplots.
    -   **Swarm-Plots:** Transparente Einzelpunkte über den Balken zeigen die wahre Verteilung.
    -   **Prozent-Achsen:** Umstellung auf `.1%` für bessere Lesbarkeit.

3.  **Interpretation Feature Importance:**
    -   **Balkenhöhe:** "Mean Decrease Accuracy" (Wirkstärke).
    -   **Schwarze Linie (Error Bar):** Unsicherheit. Lang = Feature ist nur zufällig wichtig (Rauschen).
    -   **Negative Werte:** Feature schadet dem Modell (Overfitting auf Noise) -> Kandidat für Rauswurf.

## 10.02.2026
Feature Importance vs. Risikoverteilung (Das Gender-Paradoxon):
Obwohl in den Plots (Balkendiagramm) klare Unterschiede im Risiko zwischen Männern und Frauen zu sehen sind, zeigt die Feature Importance für "gender" oft den Wert 0.
Erklärung:
- **Korrelation (Bild):** Frauen haben im Datensatz ein anderes durchschnittliches Risiko, aber das liegt oft an Drittfaktoren (z.B. sind sie im Schnitt älter).
- **Kausalität/Wichtigkeit (CSV):** Das Modell erkennt, dass "Geschlecht" keine *eigene* Vorhersagekraft bringt, wenn man Alter und BMI schon kennt. Es ignoriert das Geschlecht also zugunsten der "echten" Treiber.

Das ist ein Zeichen dafür, dass das Modell robust ist und sich nicht von Schein-Korrelationen täuschen lässt.

Robustness Testing:
Implementierung eines Loops (30 Iterationen), der bei jedem Durchlauf:
1. Ein neues Trainings-Subset zieht (Sampling Variation).
2. Ein neues Modell trainiert.
3. Feature Importance berechnet.
4. Metriken (F1, Accuracy, Precision, Recall) speichert.
Ergebnis: Saubere Trennung zwischen Test-Läufen (run_test) und echten Experimenten, automatische Ablage der Reports nach Zeitstempel und Generierung von PNGs pro Run.

Tech-Note: Feature Importance Strategie (Single vs. Loop):
Eine einzelne Analyse nutzt `n_repeats=10`, während der Loop nur `n_repeats=2` nutzt. Das ist statistisch vergleichbar und im Loop sogar überlegen:
- **Single Run:** 1 Modell * 10 Repeats = 10 Messpunkte (Fokus: stabilität dieses einen Modells).
- **Loop:** 30 Modelle * 2 Repeats = 60 Messpunkte (Fokus: Globale Stabilität über verschiedene Trainings-Sets).
Der Loop ist also trotz kleinerer Zahl pro Run insgesamt aussagekräftiger ("Law of Large Numbers").

> **Warum das Gesetz der großen Zahlen hier wirkt:**
> Das Gesetz besagt, dass sich der Durchschnitt einer Stichprobe mit wachsender Größe ($N=30$) dem wahren Erwartungswert annähert. 
> Bei einem *einzelnen* Run kann eine hohe Feature Importance Zufall sein (z.B. weil der Random Seed gerade diese Samples gewählt hat).
> Durch die Wiederholung über 30 unabhängige Trainings-Sets mitteln sich diese Zufallsschwankungen ("Rauschen") heraus. Was übrig bleibt, ist das **echte Signal**: Wenn ein Feature über 30 verschiedene Szenarien hinweg wichtig bleibt, dann ist es *wirklich* universell relevant und kein Artefakt eines einzelnen Trainingsvorgangs.

Design-Entscheidung: Fixes Validierungs-Set in den Loops:
Wir variieren bewusst nur das Trainings-Set (Resampling), während das Validierungs-Set (`X_val_robust`) für alle 30 Runs identisch bleibt.
- Grund: Wir wollen die Varianz des Modells messen, nicht die Varianz der Testdaten.
- Effekt: Wenn sich Metriken ändern, liegt es eindeutig am Training/Modell, nicht daran, dass ein Test-Set zufällig "leichter" oder "schwerer" war. Das sichert die Vergleichbarkeit ("Ceteris paribus").

## 03.02.2026
neue file: tab_pfn_v2_robustness
füge weight hinzu aus inputevents (admission of )
Feedback von Chatty: fokus auf hosp und ed data. Bei ICU sind es intensiv patienten, welche eine stark selektierte Gurppe (Kränkeste Patienten) ist. Also bei hosp und ed bleiben.
Gewicht / Größe messen von der Baseline (erste Aufnahme). 

BMI-Beobachtung:
result_name	total_measurements	unique_patients
0	BMI (kg/m2)	1901496	153725
1	Weight (Lbs)	2145353	166872
2	Height (Inches)	814964	148359
Es wird der eingetragene BMI genommen, da er mehr Patienten abdeckt 153725 gegen 148359 (height) was bei einer eigenen Berechnung zu max 148359 BMI Werten führen würde.
Da die Patienten über die Zeit mehrere Einträge haben wird für die Berechnung der Median (liegt in der Mitte von oberen 50% und unteren 50%) BMI wert benutzt = robuster.

Beobachtung nach BMI implementierung (früh, Früh ist von 60% auf 70% gesprungen)

## 27.01.2026
Diskussion mit Oliver, Daten sind verteilt (viele Gesunde und wenige kranke). Im Training sind die Daten balanciert also 1/3 jeder Kategorie. Das Model lernt muster und wendet diese auf den originellen Datensatz an, daher fallen auch viele gesunde in "früh" oder "spät" statt gesund. (Type2 error). 
- Man könnte die Features aufteilen also welche Art von Insurance, welche gender (m oder w), etc um mehr Analysewerte "Verständnis" zu bekommen.
- Veralgemeinerung nicht nur Herzfehler, sondern auch andere Diagnosen.
- Usability, wir würde man das Modell nutzen (Storyline)

## 26.01.2026
Feedback mit Jochen
Log über die Ergebinsse speichern.
Neue Notebooks für XGBoost und soweiter
Type 1 und Type 2 Error, welcher Fehler ist bevorzugt? -> Sind die Fehler für Kategorie gleich?
verschiedene Samples für Robustheit
-> 30 Durchläufe und Logs vergleichen
-> verschiedene 300 sample, kommt immer das selbe raus würde man sagen dann ist das System robust
-> Validieren mit einmal 10k Zeilen durchlaufen lassen
-> Verteilung der Range, Logs gut darstellen. AVG und Varianz
-> alles auf I50 Diagnose und dann als i-tüpfelchen andere Diagnosen testen.

## 22.01.2026
TabPFN blockiert lokale CPU-Berechnungen bei mehr als 1.000 Samples, weil die Performance dort massiv einbricht. Da du 9.000 Samples hast und eine Lizenz besitzt, ist die lokale CPU-Nutzung der falsche Weg.
Entscheidung Cloud oder lokale Maschine (MacBook M4). Cloud geht nicht weil DUA (Data Use Agreement)
Gemini:
Du hast jetzt aber ein technisches Hindernis: TabPFN hat eine Sicherheitssperre für Datensätze über 1.000 Zeilen eingebaut, weil die Rechenzeit quadratisch steigt. Da du 9.000 Trainingsdaten hast, wird dein aktueller Code sofort mit einem RuntimeError abbrechen.

Wir müssen diese Sperre manuell umgehen ("override") und die Vorhersage in kleine Häppchen ("Batches") zerlegen, damit dein Mac nicht einfriert.

Hier ist der vollständige, angepasste Code für Zelle 16/17. Er ersetzt deinen bisherigen Block komplett.

## 21.01.2025
Bei der erstellung der Klassen für Target 0-2, ob ein Patient mit code I50 (Herzfehler), wieder eintrifft wurden erst die Zeiträume. Weniger 1 Jahr und Mehr als 1 Jahr, sonstiges gewählt. Dabei verteilten sich die Daten wie folgt:
shape: (3, 2)  
┌────────┬────────┐  
│ target ┆ counts │  
│ ---    ┆ ---    │  
│ i32    ┆ u32    │  
╞════════╪════════╡  
│ 2      ┆ 204562 │
│ 0      ┆ 10742  │
│ 1      ┆ 8148   │
└────────┴────────┘
Daraus resultiert ein Übergewicht für Kategorie 0 (zensiert also kein Auftreten). 
### vorgehen / Lösung:
Aus dem realen Datenset wird ein Trainingsset erstellt mit einer bestimmten Verteilung.
Aus dem gesamten Datensatz eine bestimmte Anzahl (4.000) von jeder Kategorie zu nehmen. Damit wird in 3 klassen kategorisiert:
0: high risk
1: medium risk
2: low/no risk
Nach dem Training wird gegen die echten Daten getestet. 

## 27.12.2025
Heute habe ich das PCA mit dem Iris Dataset erstellt. Vielleicht macht es mehr Sinn die Patienten nach Krankeiten zu labeln. Also "HIV", "Windpoken" usw. anstatt nach einem boolean wert wie 0/1. Mit PCA könnte ich verschiedene nummerische Features herausfinden und diese auf 2-3 n_components reduzieren. Seaborn ist ein klasse visualisierungstool dazu.

