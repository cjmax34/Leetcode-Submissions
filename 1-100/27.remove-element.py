#
# @lc app=leetcode id=27 lang=python
#
# [27] Remove Element
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left_ptr, right_ptr = 0, len(nums) - 1
        non_val = 0
        while (left_ptr <= right_ptr):
            if (nums[left_ptr] != val):
                left_ptr += 1
                non_val += 1
            elif (nums[left_ptr] == val and nums[right_ptr] == val):
                right_ptr -= 1
            elif (nums[left_ptr] == val and nums[right_ptr] != val):
                nums[left_ptr], nums[right_ptr] = nums[right_ptr], nums[left_ptr]
                non_val += 1
                left_ptr += 1

        return non_val
        
# @lc code=end

