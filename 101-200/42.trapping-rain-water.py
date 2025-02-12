class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax = height[0], height[-1]
        left, right = 0, len(height)-1
        sum = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                leftMax = max(leftMax, height[left])
                sum += max(0, leftMax-height[left])
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                sum += max(0, rightMax-height[right])

        return sum