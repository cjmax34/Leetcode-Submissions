def equalPairs(grid):
    hash_tbl = {}
    sum = 0

    for row in grid:
        row_tpl = tuple(row)
        
        if row_tpl not in hash_tbl:
            hash_tbl[row_tpl] = 0

        hash_tbl[row_tpl] += 1
    
    for col in zip(*grid):
        if col in hash_tbl:
            sum += hash_tbl[col]

    return sum