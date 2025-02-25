# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for lst in lists:
            while lst:
                min_heap.append(lst.val)
                lst = lst.next

        if not min_heap:
            return

        heapq.heapify(min_heap)

        head = ListNode()
        temp1 = ListNode(heapq.heappop(min_heap))
        head.next = temp1
        
        while min_heap:
            temp2 = ListNode(heapq.heappop(min_heap))
            temp1.next = temp2
            temp1 = temp2
               
        return head.next