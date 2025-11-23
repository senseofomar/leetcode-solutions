# Best & Cleanest (Single Pass)
def roman_to_int(s: str) -> int:
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev = 0

    for ch in reversed(s):       # process from right to left
        curr = values[ch]
        if curr < prev:          # subtraction case
            total -= curr
        else:
            total += curr
        prev = curr

    return total
