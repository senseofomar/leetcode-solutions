# Dynamic Programming (Iterative)

def rob(nums: list[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])

    return dp[-1]


# Space Optimized (O(1) Space)

def rob2(nums: list[int]) -> int:
    prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
    for money in nums:
        new_rob = max(prev1, prev2 + money)
        prev2, prev1 = prev1, new_rob
    return prev1
