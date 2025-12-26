import duckdb as ddb
import os
from glob import glob

write_db = True

if write_db:
    # Get repository root directory
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(repo_root, "data", "mimic_v2.db")
    
    # Schritt 1: Verbindung zum Erstellen der Views
    con = ddb.connect(database=db_path)
    count = 0

    paths = {
        'ed': os.path.join(repo_root, 'data/raw/ed'),
        'hosp': os.path.join(repo_root, 'data/raw/hosp'),
        'icu': os.path.join(repo_root, 'data/raw/icu')
    }

    try:
        for schema, path in paths.items():
            # create schema if not exists
            con.execute(f"CREATE SCHEMA IF NOT EXISTS {schema};")
            csv_files = sorted(glob(os.path.join(path, '*.csv')))
            print(f"Found {len(csv_files)} csv files in {path} for schema {schema}")
            for p in csv_files:
                count += 1
                # derive a safe view name from filename
                fname = os.path.splitext(os.path.basename(p))[0]
                view_name = ''.join(c if c.isalnum() else '_' for c in fname).lower()
                full_view = f"{schema}.{view_name}"
                # create or replace view pointing to the CSV (use absolute path)
                abs_path = os.path.abspath(p)
                sql = f"CREATE OR REPLACE VIEW {full_view} AS SELECT * FROM read_csv_auto('{abs_path}');"
                try:
                    con.execute(sql)
                    print(f"View-Nr.:{count} Created view {full_view} -> {abs_path}")
                except Exception as e:
                    print(f"Failed to create view {full_view} for {p}: {e}")
    finally:
        # Sauber schließen
        con.close()
        print('Views erstellt und Verbindung geschlossen.')