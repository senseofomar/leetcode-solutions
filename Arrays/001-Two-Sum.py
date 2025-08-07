# Problem: https://leetcode.com/problems/two-sum/
# Difficulty: Easy
# Topic: Arrays, Hash Table

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i