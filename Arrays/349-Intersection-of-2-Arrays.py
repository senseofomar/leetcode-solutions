def intersection_of_2_arrays(nums1:list[int], nums2:list[int])->list[int]:
    clean_1 = sorted(nums1)
    clean_2 = sorted(nums2)
    intersection = []
    for n in clean_1:
        for m in clean_2:
            if n==m:
                intersection.append(m)
    return intersection

print(intersection_of_2_arrays([1,2,4,5],[2,4,1]))


def intersection_of_2_arrays349(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1) & set(nums2))  # & gives set intersection

print(intersection_of_2_arrays349([1,2,4,5,4],[2,4,1,4]))



from collections import Counter

def intersection_of_2_arrays350(nums1: list[int], nums2: list[int]) -> list[int]:
    count1 = Counter(nums1)    # Step 1: count frequencies of nums1
    intersection = []          # Step 2: empty result list

    for num in nums2:          # Step 3: check each element in nums2
        if count1[num] > 0:    # Step 4: if num exists in count1 and not "used up"
            intersection.append(num)  # Step 5: add it to result
            count1[num] -= 1   # Step 6: consume one occurrence
    return intersection
