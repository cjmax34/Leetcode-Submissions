def matrixSum(nums):
    sum = 0
    
    for num in nums:
        num.sort(reverse=True)

    for num in list(zip(*nums)):
        sum += max(num)

    return sum