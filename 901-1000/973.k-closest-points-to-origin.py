import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for point in points:
            euc_distance = point[0]**2 + point[1]**2
            max_heap.append((euc_distance, point))

        heapq.heapify(max_heap)

        return [heapq.heappop(max_heap)[1] for _ in range(k)] 