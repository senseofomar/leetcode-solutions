def shuffle(nums, n):
    res = []
    for i in range(n):
        res.append(nums[i])     # x_i
        res.append(nums[i+n])   # y_i
    return res
