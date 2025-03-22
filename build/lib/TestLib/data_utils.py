def normalize_data(data):
    """Normalizuje listę liczb do zakresu [0, 1]."""
    min_val, max_val = min(data), max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]
