# Sum Formula Math
def missing_number(nums: list[int]) -> int:
    n = len(nums)
    expected = n * (n + 1) // 2
    actual = sum(nums)
    return expected - actual

# Best Xor
def missing_number1(nums: list[int]) -> int:
    result = 0
    n = len(nums)

    for i in range(n + 1):
        result ^= i

    for num in nums:
        result ^= num

    return result
