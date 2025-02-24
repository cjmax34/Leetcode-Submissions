import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Simulate max heap
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones) # Create max heap

        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)

            if y != x:
                heapq.heappush(stones, y-x)

        return -stones[0] if stones else 0