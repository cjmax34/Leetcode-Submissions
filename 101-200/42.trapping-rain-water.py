class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        sum = 0

        leftMax[0], rightMax[-1] = height[0], height[-1]

        for i in range(n):
            leftMax[i] = max(leftMax[i-1], height[i])

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i])

        print(rightMax)

        for i in range(n):
            sum += min(leftMax[i], rightMax[i]) - height[i]

        return sum