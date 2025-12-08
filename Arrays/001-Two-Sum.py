# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Arrays, Hash Table

# class Solution(object):
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         seen = {}
#         for i in range(len(nums)):
#             num = nums[i]
#             complement = target - num
#             if complement in seen:
#                 return [seen[complement], i]
#             seen[num] = i


def two_sum_brute(nums : list[int], target : int) -> tuple[int, int] | None:
    for i in range(len(nums)):   #for i, num in enumerate(nums):
        num = nums[i]            #just for improving readability
        complement = target - num
        for j in range(len(nums)):
            num = nums[j]
            if j != i and nums[j] == complement:
                return i, j
    return None

"""
for i, num in enumerate(nums):
    complement = target - num
    for j, other in enumerate(nums):
        if i != j and other == complement:
            return i, j
"""

print (two_sum_brute([1,2,4], 3))


def two_sum_hash(nums : list[int], target : int) -> list[int] | None:
    seen = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num]= i
    return None

"""
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
"""

print (two_sum_hash([1,7,4], 11))