"""
Preprocessing-Logik in Funktion packen

splitting & balancing
"""

# fs_thesis/features.py
import polars as pl
import pandas as pd
from fs_thesis import sql

from sklearn.model_selection import train_test_split

def preprocess_data(data):
    # Split (train, val,)
    # 1. Konvertierung für Scikit-Learn (Split-Logik)
    df_pd = data.to_pandas()

    # Erster Split: Trenne das Test-Set ab (20% Hold-out)
    df_train_val_raw, df_test = train_test_split(
        df_pd, 
        test_size=0.2, 
        stratify=df_pd["target"], 
        random_state=42
    )

    # Zweiter Split: Trenne den Rest in Training und Validierung (z.B. 80/20 vom Rest)
    df_train, df_val = train_test_split(
        df_train_val_raw, 
        test_size=0.2, 
        stratify=df_train_val_raw["target"], 
        random_state=42
    )
    print(f"Shapes -> Train: {df_train.shape}, Val: {df_val.shape}, Test: {df_test.shape}")
    return df_train, df_val, df_test


def balance_data(df_train, n_samples=3000):
    # Zurück zu Polars für effizientes Sampling
    if isinstance(df_train, pd.DataFrame):
        df_pl = pl.from_pandas(df_train)
    else:
        df_pl = df_train
        
    classes = df_pl['target'].unique().to_list()
    chunks = []
    
    for c in classes:
        # Filter auf Klasse
        subset = df_pl.filter(pl.col("target") == c)
        # Nimm min(n_samples, echte_anzahl) -> kein Crash bei kleinen Klassen
        n_take = min(n_samples, subset.height)
        chunks.append(subset.sample(n=n_take, seed=42))
        
    df_balanced = pl.concat(chunks).sample(fraction=1.0, shuffle=True, seed=42)
    return df_balanced

def get_X_y(df, feature_cols=None, target_col="target"):
    if feature_cols is None:
        # Default Features falls keine angegeben
        feature_cols = ["gender", "anchor_age", "insurance", "language", "marital_status", "race", "admission_type", "bmi"]
    
    # Sicherstellen, dass wir Pandas für Scikit-Learn/TabPFN haben
    if isinstance(df, pl.DataFrame):
        df = df.to_pandas()
        
    X = df[feature_cols]
    y = df[target_col].values
    return X, y