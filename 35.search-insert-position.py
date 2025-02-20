class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid = (left+right)//2

        while left <= right:
            if nums[mid] < target:
                left += 1
            elif nums[mid] > target:
                right -= 1
            else:
                return mid
            mid = (left+right)//2

        return left