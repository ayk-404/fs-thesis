import unittest
from duckdb import df
from fs_thesis.data_loader import load_final_data


class TestCodeIsTested(unittest.TestCase):

    def test_unique_subject_ids(self):
        # Prüft auf Unique-Status
        df = load_final_data()
        is_unique = df["subject_id"].n_unique() == df.height
        self.assertTrue(is_unique)



if __name__ == '__main__':
    unittest.main()
