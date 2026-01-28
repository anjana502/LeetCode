# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        prev = None
        curr = head
        count = 0

        while (curr != None and count < 2):
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            count += 1
        
        head1 = self.swapPairs(curr)
        head.next = head1

        return prev