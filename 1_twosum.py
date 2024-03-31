def twoSum(nums, target):
    hash_tbl = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_tbl:
            return [hash_tbl[complement], i]
        hash_tbl[nums[i]] = i

    return []