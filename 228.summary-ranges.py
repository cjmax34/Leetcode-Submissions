class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if (not nums):
            return []
        
        res = []
        start, end = nums[0], nums[0]

        for i in range(1, len(nums)):
            if nums[i] != 1 + nums[i - 1]:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + "->" + str(end))
                start, end = nums[i], nums[i]
            else:
                end = nums[i]

        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))

        return res