def largestAltitude(gain):
    res, accumulator = 0, 0

    for num in gain:
        accumulator += num
        res = max(res, accumulator)

    return res