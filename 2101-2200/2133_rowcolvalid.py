def checkValid(matrix):
    n = len(matrix)

    for i in range(n): # Check rows
        if len(set(matrix[i])) != n:
            return False

    for i in range(n): # Check columns
        col_set = set()
        for j in range(n):
            col_set.add(matrix[j][i])
        if len(col_set) != n:
            return False

    return True

print(checkValid([[1,2,3],[3,1,2],[2,3,1]]))
