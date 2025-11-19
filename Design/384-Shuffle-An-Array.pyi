import random

class Solution:

    def __init__(self, nums):
        self.original = nums[:]   # keep copy
        self.array = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        arr = self.array[:]
        n = len(arr)

        for i in range(n):
            j = random.randint(i, n - 1)
            arr[i], arr[j] = arr[j], arr[i]

        return arr
