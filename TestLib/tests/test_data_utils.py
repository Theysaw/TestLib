import unittest
from TestLib.data_utils import normalize_data, standardize_data

class TestDataUtils(unittest.TestCase):

    def test_normalize_data(self):
        data = [10, 20, 30]
        result = normalize_data(data)
        self.assertEqual(result, [0.0, 0.5, 1.0])

    def test_standardize_data(self):
        data = [10, 20, 30]
        result = standardize_data(data)
        # Wartości po standaryzacji (średnia = 0, odchylenie = 1)
        self.assertAlmostEqual(result[0], -1.2247, places=4)
        self.assertAlmostEqual(result[1], 0.0, places=4)
        self.assertAlmostEqual(result[2], 1.2247, places=4)

    def test_standardize_data_with_zero_stdev(self):
        data = [10, 10, 10]
        result = standardize_data(data)
        # W przypadku zerowego odchylenia standardowego, wynik powinien być listą zer
        self.assertEqual(result, [0, 0, 0])

if __name__ == "__main__":
    unittest.main()