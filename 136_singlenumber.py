def singleNumber(nums):
    res = 0

    for n in nums:
        res ^= n

    return res