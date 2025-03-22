import statistics

def normalize_data(data):
    """Normalizuje listę liczb do zakresu [0, 1]."""
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]

def standardize_data(data):
    """Standaryzuje listę liczb do średniej 0 i odchylenia standardowego 1."""
    mean = statistics.mean(data)
    stdev = statistics.stdev(data)
    if stdev == 0:
        # Unikamy dzielenia przez 0 (w przypadku, gdy wszystkie wartości są równe)
        return [0 for _ in data]
    return [(x - mean) / stdev for x in data]