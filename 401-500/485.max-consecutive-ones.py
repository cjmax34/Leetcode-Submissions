class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, counter = 0, 0
        
        for n in nums:
            if n == 0:
                res = max(res, counter)
                counter = 0
            else:
                counter += 1

        return max(res, counter)