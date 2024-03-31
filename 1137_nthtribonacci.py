def tribonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    t0, t1, t2 = 0, 1, 1
    sum = 0    

    for i in range(n-2):
        sum = t0 + t1 + t2
        t0, t1, t2 = t1, t2, sum

    return sum