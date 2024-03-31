def countBits(n):
    res = []
    for i in range(n+1):
        res.append(bin(i).count('1'))
    return res

print(countBits(5))