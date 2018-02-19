import unittest
from source.code.data_loader import DataLoader


class DataLoaderTest(unittest.TestCase):

    def setUp(self):
        self.data_paths = [
            '../../data/train/allbp.data.txt'
        ]
        self.columns_path = '../../data/description/columns'
        self.classes_path = '../../data/description/classes'
        self.data_loader = DataLoader(self.data_paths, self.columns_path, self.classes_path)

    def test_data_loading_case_1(self):
        df = self.data_loader.load()
        self.assertEqual(30, len(df.columns))


if __name__ == '__main__':
    unittest.main()
