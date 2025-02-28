from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        count_list = []
        res = []
        
        for num in counts:
            count_list.append((-counts[num], num))

        heapq.heapify(count_list)

        for _ in range(k):
            test = heapq.heappop(count_list)
            res.append(test[1])

        return res