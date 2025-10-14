from collections import Counter

def intersection_of_2_arrays350(nums1: list[int], nums2: list[int]) -> list[int]:
    count1 = Counter(nums1)    # Step 1: count frequencies of nums1
    intersection = []          # Step 2: empty result list

    for num in nums2:          # Step 3: check each element in nums2
        if count1[num] > 0:    # Step 4: if num exists in count1 and not "used up"
            intersection.append(num)  # Step 5: add it to result
            count1[num] -= 1   # Step 6: consume one occurrence
    return intersection
