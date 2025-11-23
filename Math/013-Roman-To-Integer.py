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

# Left-to-right
def roman_to_int2(s: str) -> int:
    values = {'I':1, 'V':5, 'X':10, 'L':50,
              'C':100, 'D':500, 'M':1000}

    total = 0

    for i in range(len(s)):
        if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
            total -= values[s[i]]       # subtraction rule
        else:
            total += values[s[i]]

    return total

# Dictionary of special cases
def roman_to_int3(s: str) -> int:
    specials = {
        "IV":4, "IX":9,
        "XL":40, "XC":90,
        "CD":100, "CM":900
    }
    values = {
        'I':1, 'V':5, 'X':10, 'L':50,
        'C':100, 'D':500, 'M':1000
    }

    i = 0
    total = 0

    while i < len(s):
        if i + 1 < len(s) and s[i:i+2] in specials:
            total += specials[s[i:i+2]]
            i += 2
        else:
            total += values[s[i]]
            i += 1

    return total
