def kidsWithCandies(candies, extraCandies):
    res = []

    for i in candies:
        if i + extraCandies >= max(candies):
            res.append(True)
        else:
            res.append(False)

    return res