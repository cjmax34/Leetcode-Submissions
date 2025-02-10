class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for nums in intervals:
            if len(ans) == 0 or nums[0] > ans[-1][1]:
                ans.append(nums)
            else:
                ans[-1][1] = max(nums[1], ans[-1][1])

        return ans