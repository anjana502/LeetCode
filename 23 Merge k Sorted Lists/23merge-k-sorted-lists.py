import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        heapq.heapify(q)
        head = ListNode(-1)
        temp = head

        for i in range(len(lists)):
            if (lists[i] != None):
                heapq.heappush(q, (lists[i].val, i, lists[i]))
                lists[i] = lists[i].next
        
        while (len(q) != 0):
            val, i, node = heapq.heappop(q)
            temp.next = node
            temp = temp.next

            if (lists[i] != None):
                heapq.heappush(q, (lists[i].val, i, lists[i]))
                lists[i] = lists[i].next
        
        head = head.next

        return head