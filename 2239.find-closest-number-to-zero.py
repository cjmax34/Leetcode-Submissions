#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest_num = nums[0]
        for num in nums:
            if abs(num) < abs(closest_num):
                closest_num = num
            elif abs(num) == abs(closest_num):
                closest_num = max(closest_num, num)

        return closest_num

        
# @lc code=end

