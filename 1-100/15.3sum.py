class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        nums.sort()

        for i in range(n):
            x = nums[i] * -1
            j, k = i+1, n-1

            while j < k:
                if nums[j] + nums[k] > x:
                    k -= 1
                elif nums[j] + nums[k] < x:
                    j += 1
                else: 
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1

        return list(res)