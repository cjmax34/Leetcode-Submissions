# def climbingStairs(n): # iterative
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b

#     return b

def climbingStairs(n):  # Time: O(n), Space: O(1)
    if n <= 3:
        return n    # Number of ways is always n, for n <= 3
    
    prev1 = 3
    prev2 = 2
    cur = 0

    for _ in range(3, n):
        cur = prev1 + prev2
        prev2 = prev1
        prev1 = cur
    
    return cur

print(climbingStairs(5))