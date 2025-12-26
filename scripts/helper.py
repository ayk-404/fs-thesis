import polars as pl
import pandas as pd
import os
import duckdb as ddb

import sys
sys.path.insert(0, '../fs_thesis')

# Initialize connection once
repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(repo_root, "data", "mimic_v2.db")
con = ddb.connect(database=db_path, read_only=True)

def sql(query: str) -> pl.DataFrame:
    """Run a SQL query and return a Polars DataFrame."""
    pl.Config.set_tbl_rows(-1)
    pl.Config.set_tbl_cols(-1)
    try:
        return con.execute(query).pl()
    except Exception as e:
        print(f"SQL query failed: {e}")
        return pl.DataFrame()
    
def show(df: pl.DataFrame, limit: bool = False):
    """Display a Polars DataFrame with configurable column width and row limit."""
    if limit:
        pd.set_option("display.max_colwidth", 50)
        pd.set_option("display.max_rows", 20)
    else:
        pd.set_option("display.max_colwidth", None)
        pd.set_option("display.max_rows", None)
    display(df.to_pandas())