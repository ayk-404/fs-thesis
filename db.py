import duckdb
import pandas as pd

con = duckdb.connect()

con.execute("select * from 'files/mimic-iv-3.1/hosp/*.csv' limit 10").df()