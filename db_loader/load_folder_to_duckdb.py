"""
Lade einen zusätzlichen Ordner mit CSVs in deine DuckDB
"""

import duckdb
import glob
import os
from pathlib import Path

# ============================================================================
# KONFIGURATION - HIER ANPASSEN!
# ============================================================================

# Deine bestehende DuckDB
DUCKDB_FILE = "mimic_analyse.db"

# Neuer Ordner mit CSVs (z.B. der zweite MIMIC-Ordner)
NEUER_ORDNER = "/Users/andrey/Code-Kitchen/fs-thesis/files/mimic-iv-3.1/icu"  # ← ANPASSEN!

# Optional: Präfix für Tabellennamen (z.B. "icu_" für ICU-Daten)
TABELLEN_PREFIX = "icu_"  # Leer lassen für kein Präfix: ""

# ============================================================================

print("="*80)
print("ORDNER IN DUCKDB LADEN")
print("="*80)
print(f"Datenbank: {DUCKDB_FILE}")
print(f"Neuer Ordner: {NEUER_ORDNER}")
print(f"Tabellen-Präfix: '{TABELLEN_PREFIX}'")
print("="*80)

# Verbindung öffnen
con = duckdb.connect(DUCKDB_FILE)

# CSVs finden
csv_files = sorted(glob.glob(f"{NEUER_ORDNER}/*.csv"))

if not csv_files:
    print(f"❌ FEHLER: Keine CSV-Dateien in {NEUER_ORDNER} gefunden!")
    exit(1)

print(f"\n📁 Gefundene Dateien: {len(csv_files)}\n")

# Jede Datei laden
erfolg = 0
fehler = 0

for idx, file_path in enumerate(csv_files, 1):
    dateiname = os.path.basename(file_path)
    tabellen_name = dateiname.replace('.csv', '')
    
    # Präfix hinzufügen
    if TABELLEN_PREFIX:
        voller_name = f"{TABELLEN_PREFIX}{tabellen_name}"
    else:
        voller_name = tabellen_name
    
    # Größe checken
    size_mb = os.path.getsize(file_path) / (1024 * 1024)
    
    print(f"[{idx}/{len(csv_files)}] Lade: {dateiname} ({size_mb:.1f} MB)")
    print(f"    → Tabellenname: {voller_name}")
    
    try:
        # Prüfen ob Tabelle bereits existiert
        existing = con.execute(f"""
            SELECT name FROM sqlite_master 
            WHERE type='table' AND name='{voller_name}'
        """).fetchall()
        
        if existing:
            print(f"    ⚠️  Tabelle '{voller_name}' existiert bereits!")
            overwrite = input(f"    Überschreiben? (j/n): ").lower()
            if overwrite != 'j':
                print(f"    ⏭️  Übersprungen")
                continue
        
        # Tabelle erstellen
        con.execute(f"""
            CREATE OR REPLACE TABLE {voller_name} AS
            SELECT * FROM read_csv_auto('{file_path}')
        """)
        
        # Zeilen zählen
        zeilen = con.execute(f"SELECT COUNT(*) FROM {voller_name}").fetchone()[0]
        print(f"    ✅ Geladen: {zeilen:,} Zeilen")
        erfolg += 1
        
    except Exception as e:
        print(f"    ❌ FEHLER: {str(e)[:100]}")
        fehler += 1

# Zusammenfassung
print("\n" + "="*80)
print("ZUSAMMENFASSUNG")
print("="*80)
print(f"✅ Erfolgreich geladen: {erfolg}")
print(f"❌ Fehler: {fehler}")

# Alle Tabellen anzeigen
print("\n📋 Alle Tabellen in der Datenbank:")
alle_tabellen = con.execute("SHOW TABLES").df()
print(alle_tabellen.to_string(index=False))

print("\n" + "="*80)
print("✅ FERTIG!")
print("="*80)
print(f"\n💡 Deine Datenbank: {DUCKDB_FILE}")
print(f"   Gesamt Tabellen: {len(alle_tabellen)}")
print("\nJetzt kannst du mit den neuen Tabellen arbeiten:")
print(f"  con.execute('SELECT * FROM {TABELLEN_PREFIX}tabellenname LIMIT 10').df()")

# Connection schließen
con.close()