# def getAverages(nums, k):
#     cur = 0
#     n = len(nums)
#     res = [-1] * n
#     x = 2*k + 1

#     for i in range(n):
#         cur += nums[i]
#         if i >= 2*k:
#             if i > 2 *k:
#                 cur -= nums[i - 2*k - 1]
#             res[i - k] = cur // x

#     return res

# Somehow this implementation has better time and space complexities
def getAverages(nums, k):
    cur = 0
    n = len(nums)
    res = [-1] * n
    x = 2*k + 1

    for i in range(n):
        cur += nums[i]
        if i > 2*k:
            cur -= nums[i - 2*k - 1]
            res[i - k] = cur // x
        elif i == 2*k:
            res[i - k] = cur // x

    return res