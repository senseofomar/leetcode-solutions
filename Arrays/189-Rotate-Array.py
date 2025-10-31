# Using Slicing (Pythonic)
def rotate(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:] + nums[:-k]

# In-place Reversal Trick (Best Interview Solution)
def rotate1(nums, k):
    n = len(nums)
    k %= n  # handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: reverse entire array
    reverse(0, n - 1)
    # Step 2: reverse first k elements
    reverse(0, k - 1)
    # Step 3: reverse the rest
    reverse(k, n - 1)

# Using Extra Array (Simple but not in-place)
def rotate2(nums, k):
    n = len(nums)
    k %= n  # handle k > n

    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    # Step 1: reverse entire array
    reverse(0, n - 1)
    # Step 2: reverse first k elements
    reverse(0, k - 1)
    # Step 3: reverse the rest
    reverse(k, n - 1)
