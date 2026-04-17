# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        temp = head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next
        
        return count
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        count = self.countNodes(head)

        if (count < k):
            return head
        
        i = 0
        prev = None
        curr = head

        while (curr != None and i < k):
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            i += 1
        
        head1 = self.reverseKGroup(next1, k)
        head.next = head1

        return prev