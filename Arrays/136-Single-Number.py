

# Math Trick
def single_number1(nums: list[int]) -> int:
    return 2 * sum(set(nums)) - sum(nums)

# Bitwise XOR (Best & Optimal) Interview
def single_number2(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num  # XOR cancels out duplicates
    return result

#my try

def single_number3(nums: list[int])-> int:
    count = {}
    for num in nums:
        if num not in count:              #count[num] = count.get(num, 0) + 1
            count[num] = 1                #This is a shortcut for:
        else :                            #if num not in count:
            count[num] += 1               #count[num] = 1
    for key in count:                     #else:
        if count[key] ==1:                #count[num] += 1
            return key

    # satisfy type checker - Good Practice
    raise ValueError("No unique number found.")
nums1 = [1,1,2,3,2]

print(single_number3(nums1))