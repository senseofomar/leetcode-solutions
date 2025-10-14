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



