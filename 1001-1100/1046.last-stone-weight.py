import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Simulate max heap
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones) # Create max heap

        while len(stones) > 1:
            y = abs(heapq.heappop(stones))
            x = abs(heapq.heappop(stones))

            if
            res = -(y-x)
            heapq.heappush(stones, res)

        if len(stones) == 0:
            return 0

        return abs(stones[0])