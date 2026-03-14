import unittest
from duckdb import df
from fs_thesis.data_loader import load_final_data
import torch


class TestCodeIsTested(unittest.TestCase):

    def test_unique_subject_ids_final_dataset(self):
        # Prüft auf Unique-Status
        df = load_final_data()
        is_unique = df["subject_id"].n_unique() == df.height
        self.assertTrue(is_unique)

    def test_msp_for_tabPFN_training(self):
        self.assertTrue(torch.backends.mps.is_built())
        self.assertTrue(torch.backends.mps.is_available())

    # Weitere Tests können hier hinzugefügt werden, z.B.:
    # - Test auf erwartete Spaltennamen
    # - Test auf erwartete Datentypen
    # - Test auf fehlende Werte in kritischen Spalten (z.B. subject_id)
    # - Test auf erwartete Wertebereiche (z.B. anchor_age > 0)
    # - Test auf erfolgreiche feature engineering (z.B. BMI-Werte korrekt berechnet)



if __name__ == '__main__':
    unittest.main()
