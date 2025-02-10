class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])

        top_wall = 0
        bottom_wall = m
        left_wall = 0
        right_wall = n
    
        ans = []

        while left_wall < right_wall and top_wall < bottom_wall:
            # Right
            for i in range(left_wall, right_wall):
                ans.append(matrix[left_wall][i])
            top_wall += 1

            # Down
            for i in range(top_wall, bottom_wall):
                ans.append(matrix[i][right_wall - 1])
            right_wall -= 1

            if not (left_wall < right_wall and top_wall < bottom_wall):
                break

            # Left
            for i in range(right_wall - 1, left_wall - 1, -1):
                ans.append(matrix[bottom_wall - 1][i])
            bottom_wall -= 1

            # Up
            for i in range(bottom_wall - 1, top_wall - 1, -1):
                ans.append(matrix[i][left_wall])
            left_wall += 1

        return ans