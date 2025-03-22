import unittest
from TestLib.math_tools import factorial

class TestMathTools(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()
