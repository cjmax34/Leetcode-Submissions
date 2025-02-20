def deleteGreatestValue(grid):
    sum = 0
    
    for nums in grid:
        nums.sort(reverse=True)

    for nums in list(zip(*grid)):
        sum += max(nums)

    return sum