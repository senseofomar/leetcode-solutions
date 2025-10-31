# Hash Map / Counter

from collections import Counter

def single_number(nums: list[int]) -> int:
    count = Counter(nums)
    for num, freq in count.items():
        if freq == 1:
            return num
