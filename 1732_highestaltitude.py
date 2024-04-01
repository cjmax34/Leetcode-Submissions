def largestAltitude(gain):
    res, sum = 0, 0

    for num in gain:
        sum += num
        res = max(res, sum)

    return res