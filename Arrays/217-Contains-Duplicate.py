# Category	      Subtopic
# Array	          Hashing / Set lookup
#                 Data Structures → Hash Table

def contains_duplicate(nums)-> bool:
    dupli = []
    for num in nums:
        if num not in dupli:
            dupli.append(num)
        else:
            return True
    return False

def contains_duplicate1(nums) -> bool:
    seen = set()
    for num in nums:
        if num in seen:   # O(1) lookup
            return True   # duplicate found
        seen.add(num)     # store it for future checks
    return False

#one line trick
def contains_duplicate2(nums) -> bool:
    return len(nums) != len(set(nums))

numbers = [1,2,3,3,4]
print(contains_duplicate1(numbers))


