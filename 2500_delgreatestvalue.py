def deleteGreatestValue(grid):
    sum = 0
    m = grid.length     # rows length
    n = grid[0].length  # cols length

    while m and n:
        max_1 = max(grid[0])
        max_2 = max(grid[1])

        grid[0].remove(max_1)
        grid[1].remove(max_2)

        sum += max(max_1, max_2)

    return sum

print(deleteGreatestValue([[10]]))