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
