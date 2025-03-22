import unittest
from TestLib.math_tools import factorial, fibonacci

class TestMathTools(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)  # Sprawdzamy przypadek dla 0
        self.assertEqual(factorial(1), 1)  # Sprawdzamy przypadek dla 1

    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 0)    # Pierwszy wyraz Fibonacciego
        self.assertEqual(fibonacci(2), 1)    # Drugi wyraz Fibonacciego
        self.assertEqual(fibonacci(3), 1)    # Trzeci wyraz Fibonacciego
        self.assertEqual(fibonacci(4), 2)    # Czwarty wyraz Fibonacciego
        self.assertEqual(fibonacci(5), 3)    # Piąty wyraz Fibonacciego
        self.assertEqual(fibonacci(6), 5)    # Szósty wyraz Fibonacciego
        self.assertEqual(fibonacci(10), 34)  # Dziesiąty wyraz Fibonacciego
        self.assertEqual(fibonacci(0), "Input must be a positive integer")  # Błąd dla 0
        self.assertEqual(fibonacci(-5), "Input must be a positive integer")  # Błąd dla liczby ujemnej

if __name__ == "__main__":
    unittest.main()
