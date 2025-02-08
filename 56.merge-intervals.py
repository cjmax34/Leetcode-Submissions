class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for nums in intervals:
            if len(ans) == 0:
                ans.append(nums)
            else:
                if nums[0] <= ans[-1][1]:
                    ans[-1][1] = max(nums[1], ans[-1][1])
                else:
                    ans.append(nums)

        return ans