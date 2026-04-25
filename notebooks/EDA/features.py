# Imports
import sys
sys.path.insert(0, '..')
import polars as pl
import time
import json
import warnings
import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime
from tqdm.auto import tqdm

import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score, recall_score, precision_score,
    classification_report
)

from fs_thesis.data_loader import load_final_data
from fs_thesis.preprocessing import preprocess_data, balance_data, get_X_y

warnings.filterwarnings('ignore')

df = load_final_data()
#print(df.head())
#print([f"'{col}'" for col in df.columns])
# Polars syntax
print(df.select('bmi').unique().sort('bmi').head())

total = df.height
nulls = df["bmi"].null_count()

print(f"Total: {total}, Nulls: {nulls}")