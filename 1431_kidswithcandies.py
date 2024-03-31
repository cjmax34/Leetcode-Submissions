def kidsWithCandies(candies, extraCandies):
    res = []

    for i in candies:
        if i + extraCandies >= max(candies):
            res.append(True)
        else:
            res.append(False)

    return res

print(kidsWithCandies([2,3,5,1,3], 3))