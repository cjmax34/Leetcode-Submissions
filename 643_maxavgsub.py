def findMaxAverage(nums, k):
    cur = max_avg = sum(nums[0: k])
    n = len(nums)

    for i in range(n - k):
        cur += nums[i + k] - nums[i]
        max_avg = max(max_avg, cur)

    return max_avg / k