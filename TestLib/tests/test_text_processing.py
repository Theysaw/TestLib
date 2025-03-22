import unittest
from TestLib.text_processing import count_vowels, count_words

class TestTextProcessing(unittest.TestCase):

    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello World"), 3)  # 'e', 'o', 'o'
        self.assertEqual(count_vowels("Python"), 1)  # 'o'
        self.assertEqual(count_vowels("aeiouy"), 6)  # Wszystkie samogłoski
        self.assertEqual(count_vowels(""), 0)  # Pusty tekst

    def test_count_words(self):
        self.assertEqual(count_words("Hello World"), 2)  # "Hello" i "World"
        self.assertEqual(count_words("Python is awesome"), 3)  # "Python", "is", "awesome"
        self.assertEqual(count_words("This is a test."), 4)  # "This", "is", "a", "test."
        self.assertEqual(count_words(""), 0)  # Pusty tekst

if __name__ == "__main__":
    unittest.main()