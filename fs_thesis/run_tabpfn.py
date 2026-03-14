import sys, json, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))  # immer relativ zum Script selbst

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, recall_score, precision_score
from sklearn.model_selection import train_test_split
from tabpfn import TabPFNClassifier
from fs_thesis.data_loader import load_final_data
from fs_thesis.preprocessing import preprocess_data, balance_data, get_X_y

RESULTS_PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tabpfn_result.json"
N_SAMPLES = 300

df = load_final_data()
df_train, df_val, _ = preprocess_data(df)
X_val, y_val = get_X_y(df_val)

_, X_val_small, _, y_val_small = train_test_split(
    X_val, y_val, test_size=3000, stratify=y_val, random_state=42
)
X_val_small = X_val_small.reset_index(drop=True)

seed = 42
df_bal = balance_data(df_train, n_samples=N_SAMPLES, seed=seed)
X_tr, y_tr = get_X_y(df_bal)

t0 = time.time()
clf = TabPFNClassifier(device='mps', n_estimators=8)
print("fitting...")
clf.fit(X_tr, y_tr)
print("predicting...")
y_pred = clf.predict(X_val_small)
print("proba...")
y_proba = clf.predict_proba(X_val_small)

f1_pc = f1_score(y_val_small, y_pred, average=None)
result = {
    'model': 'TabPFN', 'run_id': 0, 'seed': seed,
    'accuracy': float(accuracy_score(y_val_small, y_pred)),
    'f1_macro': float(f1_score(y_val_small, y_pred, average='macro')),
    'roc_auc_macro': float(roc_auc_score(y_val_small, y_proba, multi_class='ovr', average='macro')),
    'recall_macro': float(recall_score(y_val_small, y_pred, average='macro')),
    'precision_macro': float(precision_score(y_val_small, y_pred, average='macro')),
    'f1_class_0_early': float(f1_pc[0]),
    'f1_class_1_late': float(f1_pc[1]),
    'f1_class_2_healthy': float(f1_pc[2]),
    'time_sec': time.time() - t0
}

json.dump(result, open(RESULTS_PATH, 'w'), indent=2)
print(f"✅ F1={result['f1_macro']:.4f} | AUC={result['roc_auc_macro']:.4f} | {result['time_sec']:.1f}s")