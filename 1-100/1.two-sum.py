class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash_set:
                return [hash_set[comp], i]
            hash_set[nums[i]] = i

        return []