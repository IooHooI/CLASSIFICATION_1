import unittest
from source.code import data_loader


class test_data_loader(unittest.TestCase):

    def setUp(self):
        self.data_paths = [
            '../../data/allbp.data.txt',
            '../../data/dis.data.txt'
        ]

    def test_data_loading_case_1(self):
        data_loader.load_data(self.data_paths[0])

    def test_data_loading_case_2(self):
        data_loader.load_data(self.data_paths[1])


if __name__ == '__main__':
    unittest.main()
