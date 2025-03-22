def factorial(n):
    """Zwraca silnię liczby n."""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Zwraca n-ty wyraz ciągu Fibonacciego."""
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b