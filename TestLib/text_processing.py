def count_vowels(text):
    """Zlicza samogłoski w podanym tekście."""
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in text if char in vowels)

def count_words(text):
    """Zlicza liczbę słów w podanym tekście."""
    words = text.split()  # Rozdziela tekst na słowa przy pomocy spacji
    return len(words)