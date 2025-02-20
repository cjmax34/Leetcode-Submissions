import math

def generate(rowIndex):
    res = []

    for i in range(rowIndex+1):
        if i == 0 or i == rowIndex:
            res.append(1)
        else:
            res.append(math.factorial(rowIndex)/(math.factorial(i) * math.factorial(rowIndex-i)))

    return list(map(int, res))