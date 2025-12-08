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
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        for j in range(len(nums)):
            num = nums[j]
            if j != i and nums[j] == complement:
                return i, j
    return None


print (two_sum_brute([1,2,4], 3))