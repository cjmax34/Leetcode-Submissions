class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 0
        n = len(nums) - 1

        for i in range(n):
            if nums[i] == nums [i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        for _ in nums:
            if nums[right] != 0: # swap
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1

        return nums