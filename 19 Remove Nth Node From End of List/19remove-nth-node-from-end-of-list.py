# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        slow = head
        fast = head

        for i in range(1, n):
            fast = fast.next
        
        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next
        
        if (slow == head):
            head = head.next
        
        prev.next = slow.next
        del slow

        return head