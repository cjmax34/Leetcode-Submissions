class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0] * len(nums)
        n = len(nums)
        k = k % n
        
        for i in range(k):
            res[i] = nums[n-k+i]

        for i in range(k, n):
            res[i] = nums[i-k]

        for i in range(n):
            nums[i] = res[i]