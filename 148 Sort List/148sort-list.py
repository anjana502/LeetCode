# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, head1, head2):
        if (head1 == None):
            return head2
        if (head2 == None):
            return head1
        
        if (head1.val <= head2.val):
            head1.next = self.merge(head1.next, head2)
            return head1
        else:
            head2.next = self.merge(head1, head2.next)
            return head2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        prev = head
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        head1 = slow
        prev.next = None

        head = self.sortList(head)
        head1 = self.sortList(head1)

        head = self.merge(head, head1)

        return head