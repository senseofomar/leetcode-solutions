def move_zeroes(self, nums: list[int]) -> None:
    left = 0  # points to the place where the next non-zero should go

    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
