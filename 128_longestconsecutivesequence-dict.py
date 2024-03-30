def longestConsecutive(nums):
    nums = set(nums)
    table = {}
    maxval = 0
    for num in nums:
        x = table.get(num - 1, 0)
        y = table.get(num + 1, 0)
        val = x + y + 1
        print(num, x, y, val)
        table[num - x] = val
        table[num + y] = val
        maxval = max(maxval, val)
        print(table)
    return maxval
    
longestConsecutive([100, 1, 200, 3, 4, 2])