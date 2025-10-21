def first_uniq_char(t: str) -> int:
    hashmap = {}

    # Count frequencies
    for ch in t:
        hashmap[ch] = hashmap.get(ch, 0) + 1

    # Find first character with count = 1
    for i, ch in enumerate(t):
        if hashmap[ch] == 1:
            return i

    return -1  # if no unique character


from collections import Counter

def first_uniq_char1(t: str) -> int:
    freq = Counter(t)  # counts all chars
    for i, ch in enumerate(t):
        if freq[ch] == 1:
            return i
    return -1
