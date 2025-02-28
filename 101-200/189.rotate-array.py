class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        n = len(nums)
        k = k % n       # Get modulo especially when k >> n

        reverse(0, n-1) # Reverse whole list first
        reverse(0, k-1) # Reverse first k elements
        reverse(k, n-1) # Reverse last n-k elements