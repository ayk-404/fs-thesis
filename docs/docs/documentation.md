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