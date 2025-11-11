# Simulated environment
first_bad = 4  # for example

def is_bad_version(version):
    return version >= first_bad


def first_bad_version(n):
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if is_bad_version(mid):
            right = mid  # mid might be the first bad
        else:
            left = mid + 1
    return left


# Test
print(first_bad_version(5))  # Output: 4
