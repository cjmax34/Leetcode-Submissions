class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_works(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)

            return hours <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left+right) // 2
            if k_works(mid):
                right = mid
            else:
                left = mid+1

        return left