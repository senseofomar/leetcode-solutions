def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    # handle negative numbers
    sign = -1 if x < 0 else 1
    x_str = str(abs(x))           # convert to string
    rev_str = x_str[::-1]         # reverse string
    rev_int = int(rev_str) * sign # convert back to int and restore sign

    # handle 32-bit signed integer overflow
    if rev_int < -2**31 or rev_int > 2**31 - 1:
        return 0
    return rev_int

# two pointer
def reverse2(x):
    """
    :type x: int
    :rtype: int
    """
    # Step 1: handle negative sign
    sign = -1 if x < 0 else 1
    x_str = str(abs(x))           # convert to string
    chars = list(x_str)           # make it a list for in-place modification
    # Step 2: apply two pointers to reverse
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    # Step 3: join back and convert to int
    rev_int = int("".join(chars)) * sign
    # Step 4: handle 32-bit signed integer overflow
    if rev_int < -2**31 or rev_int > 2**31 - 1:
        return 0
    return rev_int
