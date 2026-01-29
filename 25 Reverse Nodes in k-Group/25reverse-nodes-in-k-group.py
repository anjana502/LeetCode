# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countNodes(self, head):
        count = 0
        temp = head

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
        
        prev = None
        curr = head
        count = 0

        while (curr != None and count < k):
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            count += 1
        
        head.next = self.reverseKGroup(curr, k)

        return prev