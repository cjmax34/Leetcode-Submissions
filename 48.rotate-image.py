class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reverse
        for i in range(len(matrix)):
            left, right = 0, len(matrix) - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1