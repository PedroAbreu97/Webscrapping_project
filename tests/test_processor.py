import unittest
from src.processor import DataProcessor

class TestDataProcessor(unittest.TestCase):
    def setUp(self):
        self.data = [{'title': 'Item 1', 'price': '$10'}, {'title': 'Item 2', 'price': '$20'}]
        self.processor = DataProcessor(self.data)

    def test_process_data(self):
        df = self.processor.process_data()
        self.assertEqual(df['price'].iloc[0], 10.0)
        self.assertEqual(df['price'].iloc[1], 20.0)

    def test_save_data(self):
        import os
        df = self.processor.process_data()
        self.processor.save_data(df, 'data/processed/test_data.csv')
        self.assertTrue(os.path.exists('data/processed/test_data.csv'))
        os.remove('data/processed/test_data.csv')

if __name__ == '__main__':
    unittest.main()