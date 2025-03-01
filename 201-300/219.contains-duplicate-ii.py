class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashh = {}

        for idx, num in enumerate(nums):
            if num in hashh:
                if abs(idx - hashh[num]) <= k:
                    return True
            hashh[num] = idx

        return False