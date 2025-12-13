"""
CSV Daten Analyzer für Masterarbeit - MIMIC-IV Edition
Analysiert alle CSV-Dateien einzeln (verschiedene Schemas)
"""

import duckdb
import pandas as pd
import glob
import os
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Konfiguration
CSV_ORDNER = "/Users/andrey/Code-Kitchen/fs-thesis/files/mimic-iv-3.1/hosp"  # Dein Pfad
OUTPUT_ORDNER = "analyse_ergebnisse"
DUCKDB_FILE = "mimic_analyse.db"

# Output-Ordner erstellen
os.makedirs(OUTPUT_ORDNER, exist_ok=True)

# Seaborn Style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

print("="*80)
print("MIMIC-IV DATEN ANALYZER - MASTERARBEIT")
print("="*80)
print(f"Analysiere Dateien in: {CSV_ORDNER}")
print(f"Zeitpunkt: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print("="*80)

# DuckDB Connection
con = duckdb.connect(DUCKDB_FILE)

# 1. DATEI-ÜBERSICHT
print("\n📁 SCHRITT 1: Datei-Übersicht")
print("-" * 80)

csv_files = sorted(glob.glob(f"{CSV_ORDNER}/*.csv"))
print(f"Gefundene CSV-Dateien: {len(csv_files)}\n")

datei_info = []
for file in csv_files:
    size_mb = os.path.getsize(file) / (1024 * 1024)
    datei_info.append({
        'Dateiname': os.path.basename(file),
        'Größe (MB)': round(size_mb, 2),
        'Pfad': file
    })

df_dateien = pd.DataFrame(datei_info)
print(df_dateien[['Dateiname', 'Größe (MB)']].to_string(index=False))
print(f"\n📊 Gesamtgröße: {df_dateien['Größe (MB)'].sum():.2f} MB ({df_dateien['Größe (MB)'].sum()/1024:.2f} GB)")

# 2. DETAILLIERTE ANALYSE JEDER TABELLE
print("\n📊 SCHRITT 2: Detaillierte Tabellen-Analyse")
print("-" * 80)

tabellen_info = []

for idx, file in enumerate(csv_files, 1):
    tabellen_name = os.path.basename(file).replace('.csv', '')
    print(f"\n[{idx}/{len(csv_files)}] Analysiere: {tabellen_name}")
    
    try:
        # Zeilenanzahl
        zeilen = con.execute(f"SELECT COUNT(*) FROM read_csv_auto('{file}')").fetchone()[0]
        
        # Spalten-Info
        schema = con.execute(f"DESCRIBE SELECT * FROM read_csv_auto('{file}')").df()
        spalten = schema['column_name'].tolist()
        typen = schema['column_type'].tolist()
        
        # Sample Daten
        sample = con.execute(f"SELECT * FROM read_csv_auto('{file}') LIMIT 3").df()
        
        # Speichern
        tabellen_info.append({
            'Tabelle': tabellen_name,
            'Zeilen': zeilen,
            'Spalten': len(spalten),
            'Größe_MB': round(os.path.getsize(file) / (1024 * 1024), 2),
            'Schema': list(zip(spalten, typen)),
            'Sample': sample
        })
        
        print(f"  ✓ {zeilen:,} Zeilen, {len(spalten)} Spalten")
        print(f"    Spalten: {', '.join(spalten[:5])}{'...' if len(spalten) > 5 else ''}")
        
    except Exception as e:
        print(f"  ⚠️ Fehler: {str(e)[:100]}")
        tabellen_info.append({
            'Tabelle': tabellen_name,
            'Fehler': str(e)
        })

# 3. ZUSAMMENFASSUNG
print("\n📈 SCHRITT 3: Gesamtzusammenfassung")
print("-" * 80)

df_summary = pd.DataFrame([{
    'Tabelle': t['Tabelle'],
    'Zeilen': t.get('Zeilen', 0),
    'Spalten': t.get('Spalten', 0),
    'Größe (MB)': t.get('Größe_MB', 0)
} for t in tabellen_info if 'Zeilen' in t])

# Nach Größe sortieren
df_summary = df_summary.sort_values('Größe (MB)', ascending=False)
print(df_summary.to_string(index=False))

gesamt_zeilen = df_summary['Zeilen'].sum()
print(f"\n✅ GESAMT: {gesamt_zeilen:,} Zeilen über alle Tabellen")
print(f"✅ Größte Tabelle: {df_summary.iloc[0]['Tabelle']} ({df_summary.iloc[0]['Zeilen']:,} Zeilen)")

# 4. TABELLEN IN DUCKDB LADEN
print("\n💾 SCHRITT 4: Tabellen in DuckDB laden")
print("-" * 80)

erfolgreich = 0
for info in tabellen_info:
    if 'Zeilen' not in info:
        continue
    
    tabellen_name = info['Tabelle']
    file_path = f"{CSV_ORDNER}/{tabellen_name}.csv"
    
    try:
        # Jede Tabelle einzeln laden
        con.execute(f"""
            CREATE OR REPLACE TABLE {tabellen_name} AS
            SELECT * FROM read_csv_auto('{file_path}')
        """)
        erfolgreich += 1
        print(f"  ✓ {tabellen_name}: {info['Zeilen']:,} Zeilen")
        
    except Exception as e:
        print(f"  ⚠️ {tabellen_name}: Fehler - {str(e)[:80]}")

print(f"\n✅ {erfolgreich}/{len(tabellen_info)} Tabellen erfolgreich geladen")
print(f"✅ Datenbank gespeichert: {DUCKDB_FILE}")

# 5. SCHEMA-ÜBERSICHT SPEICHERN
print("\n📋 SCHRITT 5: Schema-Dokumentation erstellen")
print("-" * 80)

schema_datei = f"{OUTPUT_ORDNER}/schema_dokumentation.txt"
with open(schema_datei, 'w', encoding='utf-8') as f:
    f.write("="*80 + "\n")
    f.write("MIMIC-IV SCHEMA DOKUMENTATION\n")
    f.write(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*80 + "\n\n")
    
    for info in tabellen_info:
        if 'Schema' not in info:
            continue
            
        f.write(f"\n{'='*80}\n")
        f.write(f"Tabelle: {info['Tabelle']}\n")
        f.write(f"Zeilen: {info['Zeilen']:,}\n")
        f.write(f"Spalten: {info['Spalten']}\n")
        f.write(f"Größe: {info['Größe_MB']} MB\n")
        f.write(f"{'-'*80}\n")
        f.write("Schema:\n")
        for spalte, typ in info['Schema']:
            f.write(f"  - {spalte}: {typ}\n")
        
        f.write(f"\nBeispiel-Daten (erste 3 Zeilen):\n")
        f.write(info['Sample'].to_string())
        f.write("\n")

print(f"✅ Schema-Dokumentation: {schema_datei}")

# 6. WICHTIGE TABELLEN IDENTIFIZIEREN
print("\n🎯 SCHRITT 6: Wichtige Tabellen für ML/Analyse")
print("-" * 80)

kern_tabellen = {
    'patients': 'Patienten-Stammdaten',
    'admissions': 'Krankenhaus-Aufenthalte', 
    'labevents': 'Labor-Werte (sehr groß!)',
    'diagnoses_icd': 'Diagnosen',
    'prescriptions': 'Medikationen',
    'procedures_icd': 'Prozeduren'
}

print("\nWichtige Kern-Tabellen:")
for tabelle, beschreibung in kern_tabellen.items():
    info = next((t for t in tabellen_info if t['Tabelle'] == tabelle), None)
    if info and 'Zeilen' in info:
        print(f"  • {tabelle}: {beschreibung}")
        print(f"    → {info['Zeilen']:,} Zeilen, {info['Spalten']} Spalten")

# 7. BEISPIEL-ABFRAGEN
print("\n💡 SCHRITT 7: Beispiel-Abfragen für deine Masterarbeit")
print("-" * 80)

beispiele = """
# 1. Patienten-Übersicht
patienten = con.execute(\"\"\"
    SELECT gender, COUNT(*) as anzahl 
    FROM patients 
    GROUP BY gender
\"\"\").df()

# 2. Aufenthalte pro Jahr
aufenthalte = con.execute(\"\"\"
    SELECT 
        EXTRACT(YEAR FROM admittime) as jahr,
        COUNT(*) as anzahl
    FROM admissions
    GROUP BY jahr
    ORDER BY jahr
\"\"\").df()

# 3. Häufigste Diagnosen
diagnosen = con.execute(\"\"\"
    SELECT 
        d.long_title,
        COUNT(*) as anzahl
    FROM diagnoses_icd di
    JOIN d_icd_diagnoses d ON di.icd_code = d.icd_code
    GROUP BY d.long_title
    ORDER BY anzahl DESC
    LIMIT 10
\"\"\").df()

# 4. Daten für ML laden (mit Sampling!)
ml_data = con.execute(\"\"\"
    SELECT * FROM labevents 
    USING SAMPLE 1%  -- Nur 1% für schnelles Testen!
\"\"\").df()
"""

print(beispiele)

# 8. REPORT ERSTELLEN
print("\n📄 SCHRITT 8: Abschluss-Report")
print("-" * 80)

report_datei = f"{OUTPUT_ORDNER}/analyse_report.txt"
with open(report_datei, 'w', encoding='utf-8') as f:
    f.write("="*80 + "\n")
    f.write("MIMIC-IV ANALYSE-REPORT\n")
    f.write(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    f.write("="*80 + "\n\n")
    
    f.write(f"Analysierte Dateien: {len(csv_files)}\n")
    f.write(f"Gesamtgröße: {df_dateien['Größe (MB)'].sum():.2f} MB\n")
    f.write(f"Gesamt Zeilen: {gesamt_zeilen:,}\n\n")
    
    f.write("Top 10 größte Tabellen:\n")
    f.write(df_summary.head(10).to_string(index=False))
    f.write("\n\n")
    
    f.write("Kern-Tabellen für Analyse:\n")
    for tabelle, beschreibung in kern_tabellen.items():
        info = next((t for t in tabellen_info if t['Tabelle'] == tabelle), None)
        if info and 'Zeilen' in info:
            f.write(f"  • {tabelle}: {info['Zeilen']:,} Zeilen\n")

print(f"✅ Report gespeichert: {report_datei}")

# 9. NÄCHSTE SCHRITTE
print("\n" + "="*80)
print("🎉 ANALYSE ABGESCHLOSSEN!")
print("="*80)
print("\n📂 Generierte Dateien:")
print(f"  • DuckDB: {DUCKDB_FILE}")
print(f"  • Schema: {schema_datei}")
print(f"  • Report: {report_datei}")

print("\n🚀 Nächste Schritte für deine Masterarbeit:")
print("\n1. DATEN ERKUNDEN:")
print("   python")
print("   >>> import duckdb")
print("   >>> con = duckdb.connect('mimic_analyse.db')")
print("   >>> con.execute('SHOW TABLES').df()  # Alle Tabellen anzeigen")

print("\n2. KERN-DATEN ANALYSIEREN:")
print("   • patients: Demographie")
print("   • admissions: Aufenthalte & Outcomes")
print("   • labevents: Labor-Werte (158 Mio Zeilen!)")
print("   • diagnoses_icd: Diagnosen")

print("\n3. ML VORBEREITUNG:")
print("   • JOIN zwischen Tabellen über subject_id & hadm_id")
print("   • Feature Engineering aus Labor-Werten")
print("   • Sampling für schnelles Prototyping (USING SAMPLE X%)")

print("\n💡 TIPP: labevents ist RIESIG (17.5 GB)")
print("   → Nutze ALWAYS Sampling oder Filter!")
print("   → Beispiel: WHERE itemid IN (50912, 50931)  -- nur bestimmte Tests")

print("\n" + "="*80)

# Connection schließen
con.close()
print("✅ Fertig! Du kannst jetzt mit deiner Analyse starten! 🚀")