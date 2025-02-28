class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        res = {}

        for num in nums:
            if num not in res:
                res[num] = 1

            else:
                count += res[num]
                res[num] += 1

        return count