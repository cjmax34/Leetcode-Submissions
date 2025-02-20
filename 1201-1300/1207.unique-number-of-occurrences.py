def uniqueOccurrences(arr):
    hash_tbl = {}
    res = []

    for num in arr:
        if num not in hash_tbl:
            hash_tbl[num] = 0
        hash_tbl[num] += 1

    for num in list(hash_tbl.values()):
        if num not in res:
            res.append(num)
        else:
            return False

    return True