class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 0
        for num in nums:
            if num == curr:
                count += 1
            elif num != curr and count != 0:
                count -= 1
            elif num != curr and count == 0:
                curr = num

        return curr