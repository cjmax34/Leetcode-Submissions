class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = num_zeroes = max_width = 0
        n = len(nums)

        while right < n:
            if nums[right] == 0:
                num_zeroes += 1

            while num_zeroes > k:
                if nums[left] == 0:
                    num_zeroes -= 1
                left += 1

            w = right - left + 1
            right += 1
            max_width = max(max_width, w)
            
        return max_width