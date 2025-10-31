# Hash Map / Counter
from collections import Counter

def single_number(nums: list[int]) -> int:
    count = Counter(nums)
    for num, freq in count.items():
        if freq == 1:
            return num

# Math Trick
def single_number1(nums: list[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)

# Bitwise XOR (Best & Optimal)
def single_number2(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out duplicates
    return result
