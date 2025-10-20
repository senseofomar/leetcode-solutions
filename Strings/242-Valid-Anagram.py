def is_anagram(t: str, s: str) -> bool:
    return sorted(t.lower()) == sorted(s.lower())


def is_anagram1(t: str, s: str) -> bool:
    if len(t) != len(s):
        return False

    count = {}
    for ch in t.lower():
        count[ch] = count.get(ch, 0) + 1

    for ch in s.lower():
        if ch not in count:
            return False
        count[ch] -= 1
        if count[ch] == 0:
            del count[ch]

    return not count


from collections import Counter
def is_anagram3(t, s):
    return Counter(t.lower()) == Counter(s.lower())
