import sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, recall_score, precision_score
from tabpfn import TabPFNClassifier
from fs_thesis.data_loader import load_final_data
from fs_thesis.preprocessing import preprocess_data, balance_data, get_X_y

RESULTS_PATH = sys.argv[1] if len(sys.argv) > 1 else "/tmp/tabpfn_test_result.json"
SEED         = int(sys.argv[2]) if len(sys.argv) > 2 else 42
N_SAMPLES    = int(sys.argv[3]) if len(sys.argv) > 3 else 300

df = load_final_data()
df_train, _, df_test = preprocess_data(df)
X_test, y_test = get_X_y(df_test)

df_bal = balance_data(df_train, n_samples=N_SAMPLES, seed=SEED)
X_tr, y_tr = get_X_y(df_bal)

clf = TabPFNClassifier(device='mps', n_estimators=8)
print("fitting...")
clf.fit(X_tr, y_tr)
print("predicting test...")
y_pred = clf.predict(X_test)
print("proba test...")
y_proba = clf.predict_proba(X_test)

proba_path = RESULTS_PATH.replace('.json', '_proba.npy')
np.save(proba_path, y_proba)

f1_pc = f1_score(y_test, y_pred, average=None)
result = {
    'model': 'TabPFN',
    'best_seed': SEED,
    'val_f1': None,
    'test_accuracy': float(accuracy_score(y_test, y_pred)),
    'test_f1_macro': float(f1_score(y_test, y_pred, average='macro')),
    'test_roc_auc': float(roc_auc_score(y_test, y_proba, multi_class='ovr', average='macro')),
    'test_f1_early': float(f1_pc[0]),
    'test_f1_late': float(f1_pc[1]),
    'test_f1_healthy': float(f1_pc[2]),
    'proba_path': proba_path
}

json.dump(result, open(RESULTS_PATH, 'w'), indent=2)
print(f"✅ F1={result['test_f1_macro']:.4f} | AUC={result['test_roc_auc']:.4f}")