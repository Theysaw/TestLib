import sys
import os
import unittest
from TestLib.data_utils import normalize_data

class TestDataUtils(unittest.TestCase):
    def test_normalize_data(self):
        data = [10, 20, 30]
        result = normalize_data(data)
        self.assertEqual(result, [0.0, 0.5, 1.0])

if __name__ == "__main__":
    unittest.main()