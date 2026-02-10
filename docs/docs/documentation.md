### 10.02.2026
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

### 03.02.2026
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

### 27.01.2026
Diskussion mit Oliver, Daten sind verteilt (viele Gesunde und wenige kranke). Im Training sind die Daten balanciert also 1/3 jeder Kategorie. Das Model lernt muster und wendet diese auf den originellen Datensatz an, daher fallen auch viele gesunde in "früh" oder "spät" statt gesund. (Type2 error). 
- Man könnte die Features aufteilen also welche Art von Insurance, welche gender (m oder w), etc um mehr Analysewerte "Verständnis" zu bekommen.
- Veralgemeinerung nicht nur Herzfehler, sondern auch andere Diagnosen.
- Usability, wir würde man das Modell nutzen (Storyline)

### 26.01.2026
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

### 22.01.2026
TabPFN blockiert lokale CPU-Berechnungen bei mehr als 1.000 Samples, weil die Performance dort massiv einbricht. Da du 9.000 Samples hast und eine Lizenz besitzt, ist die lokale CPU-Nutzung der falsche Weg.
Entscheidung Cloud oder lokale Maschine (MacBook M4). Cloud geht nicht weil DUA (Data Use Agreement)
Gemini:
Du hast jetzt aber ein technisches Hindernis: TabPFN hat eine Sicherheitssperre für Datensätze über 1.000 Zeilen eingebaut, weil die Rechenzeit quadratisch steigt. Da du 9.000 Trainingsdaten hast, wird dein aktueller Code sofort mit einem RuntimeError abbrechen.

Wir müssen diese Sperre manuell umgehen ("override") und die Vorhersage in kleine Häppchen ("Batches") zerlegen, damit dein Mac nicht einfriert.

Hier ist der vollständige, angepasste Code für Zelle 16/17. Er ersetzt deinen bisherigen Block komplett.

### 21.01.2025
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

### 27.12.2025
Heute habe ich das PCA mit dem Iris Dataset erstellt. Vielleicht macht es mehr Sinn die Patienten nach Krankeiten zu labeln. Also "HIV", "Windpoken" usw. anstatt nach einem boolean wert wie 0/1. Mit PCA könnte ich verschiedene nummerische Features herausfinden und diese auf 2-3 n_components reduzieren. Seaborn ist ein klasse visualisierungstool dazu.


# Master Thesis
 • spezielle Krankheiten?
 • kleinerer Scope anfangen & skalieren (Kategorie von Diagnosen)

## Arbeit
 • Seitenanzahl egal max 70
 
## Structure
 • Motivation
 • Problem klar?
 • Frage
 • Warum ist die Frage interessant
 • strengente Analyse auf die Frage
 • Resultat
 • Was sind die take aways?
 • Was sind die nächsten Schritte?
# wichtig
Nicht sich selbst beweisen 
Sondern sauber methodisch arbeiten 

# Open Points
- Sind semantische Daten okay?
- E-Mail in PhysioNet eintrage ok? 
- HOPE keine Rückmeldung wenn nicht dann nicht? 

## Thesis Definieren:
"How good is the performance of a foundation model to predict the risk of a diagnose, based on demographic data?" 


syn. data : scop ändert sich

# Idee
Schauen Statistik wodurch menschen am häufigsten sterben und dann ml drauf
