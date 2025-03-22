def count_vowels(text):
    """Zlicza samogłoski w podanym tekście."""
    vowels = "aeiouyAEIOUY"
    return sum(1 for char in text if char in vowels)
