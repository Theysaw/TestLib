import unittest
from TestLib.text_processing import count_vowels

class TestTextProcessing(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)

if __name__ == "__main__":
    unittest.main()