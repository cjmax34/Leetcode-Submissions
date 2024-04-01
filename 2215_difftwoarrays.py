def findDifference(nums1, nums2):
    nums1_set, nums2_set = set(nums1), set(nums2)
    nums1_lst, nums2_lst = [], []

    for num in nums1_set:
        if num not in nums2_set:
            nums1_lst.append(num)

    for num in nums2_set:
        if num not in nums1_set:
            nums2_lst.append(num)

    return [nums1_lst, nums2_lst]