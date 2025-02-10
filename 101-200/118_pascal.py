def generate(numRows):
    res = []

    for i in range(numRows):
        res.append([])
        for j in range(0, i+1):
            if j == 0 or j == i:
                res[i].append(1)
            else:
                res[i].append(res[i-1][j-1] + res[i-1][j])
    return res