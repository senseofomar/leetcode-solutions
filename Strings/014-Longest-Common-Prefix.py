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
