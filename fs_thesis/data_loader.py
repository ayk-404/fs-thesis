"""
Daten-Extraktion & Preprocessing -> fs_thesis/features.py
(SQL Queries, Joins, das Berechnen von t_event und target, BMI Median)

Warum? Damit du in jedem neuen Notebook (z.B. für ein anderes Modell) einfach 
df = load_and_preprocess_data() aufrufen kannst.
Wohin speichern? Das fertige df_final DataFrame solltest du als Parquet-Datei in processed speichern.
"""

# fs_thesis/features.py
import polars as pl
from fs_thesis import sql

def load_bmi_coverage_data():
    df_coverage = sql("""
    SELECT 
        result_name, 
        COUNT(*) as total_measurements,
        COUNT(DISTINCT subject_id) as unique_patients
    FROM hosp.omr 
    WHERE result_name IN ('BMI (kg/m2)', 'Weight (Lbs)', 'Height (Inches)')
    GROUP BY result_name
    """)
    return df_coverage

def load_patients_data():
    df = sql("SELECT * from hosp.patients")
    return df

def load_admissions_data():
    df = sql("SELECT * from hosp.admissions")
    return df

def load_baseline_data():
    df_baseline = sql("""
                      SELECT 
                        p.subject_id,
                        p.gender,
                        p.anchor_age,
                        p.dod,
                        -- Daten aus der ersten Aufnahme (Baseline)
                        first_admit.admittime AS t0_time,
                        first_admit.insurance,
                        first_admit.language,
                        first_admit.marital_status,
                        first_admit.race,
                        first_admit.admission_type
                    FROM hosp.patients p
                    INNER JOIN (
                        -- Subquery, um nur die zeitlich erste Aufnahme pro Patient zu finden
                        SELECT 
                            subject_id, 
                            admittime, 
                            insurance, 
                            language, 
                            marital_status, 
                            race, 
                            admission_type,
                            ROW_NUMBER() OVER (PARTITION BY subject_id ORDER BY admittime ASC) as row_num
                        FROM hosp.admissions
                    ) first_admit ON p.subject_id = first_admit.subject_id
                    WHERE first_admit.row_num = 1""")
    return df_baseline

def load_diagnosis_data():
    data = sql("""
               SELECT 
                d.*, 
                i.long_title
               FROM hosp.diagnoses_icd d
               LEFT JOIN hosp.d_icd_diagnoses i ON d.icd_code = i.icd_code
               WHERE d.icd_code LIKE 'I50%'""")
    
    return data

def load_event_data():
    df_event = sql("""
                   SELECT 
                    d.subject_id,
                    MIN(a.admittime) AS event_time
                   FROM hosp.diagnoses_icd d
                   JOIN hosp.admissions a ON d.hadm_id = a.hadm_id
                   WHERE d.icd_code LIKE 'I50%' 
                   GROUP BY d.subject_id""")
    return df_event

def load_final_data():
    df_baseline = load_baseline_data()
    df_event = load_event_data()

    df_final = (
    df_baseline.join(df_event, on="subject_id", how="left")
    # 1. Zeitdifferenzen und Event-Indikator berechnen
    .with_columns([
        ((pl.col("event_time") - pl.col("t0_time")).dt.total_days()).alias("t_event"),
        ((pl.col("dod") - pl.col("t0_time")).dt.total_days()).alias("t_death"),
        pl.col("event_time").is_not_null().cast(pl.Int32).alias("event_occurred")
    ])
    # 2. Duration festlegen (Priorität: Event > Tod > Fallback) und Clip
    .with_columns(
        pl.coalesce([
            pl.col("t_event"),
            pl.col("t_death"),
            pl.lit(2000)
        ])
        .clip(lower_bound=0)
        .alias("duration")
    )
    # 3. Zielvariable (Target) für TabPFN definieren
    .with_columns(
        pl.when((pl.col("event_occurred") == 1) & (pl.col("duration") <= 365))
        .then(0)     # Klasse 0: Früher Ausbruch (< 1 Jahr)
        .when((pl.col("event_occurred") == 1) & (pl.col("duration") > 365))
        .then(1)     # Klasse 1: Später Ausbruch (> 1 Jahr)
        .otherwise(2) # Klasse 2: Zensiert / Gesund / Kein Event
        .alias("target")
    )
)
    return df_final