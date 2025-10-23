# Vertical scanning Interview approach
def longest_common_prefix1(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = ""
    for i in range(len(strs[0])):  # go letter by letter in first word
        ch = strs[0][i]
        for word in strs[1:]:
            if i >= len(word) or word[i] != ch:
                return prefix
        prefix += ch  # if all matched, keep adding
    return prefix

# Sorting
def longest_common_prefix2(strs: list[str]) -> str:
    if not strs:
        return ""

    strs.sort()  # Lexicographically
    first, last = strs[0], strs[-1]
    prefix = ""
    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            prefix += first[i]
        else:
            break
    return prefix

# Using zip
def longest_common_prefix3(strs: list[str]) -> str:
    prefix = ""
    for chars in zip(*strs):  # groups by position
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix
