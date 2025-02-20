def hammingWeight(n):   # 191. Number of 1 Bits
    res = 0

    while n:
        n = n & (n - 1)
        res += 1

    return res

print(hammingWeight(2147483645))