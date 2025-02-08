class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        count = 0
        while count < 4:
            n = len(mat)
            # Transpose matrix
            for i in range(n):
                for j in range(i+1, n):
                    mat[j][i], mat[i][j] = mat[i][j], mat[j][i]
            
            # Reverse matrix
            for i in range(n):
                mat[i].reverse()

            if mat == target:
                return True

            count += 1

        return False