# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if (head == None):
            return head

        prev = head
        to_delete = head

        while (to_delete != None):
            if (to_delete.val == val):
                if (prev == to_delete):
                    head = head.next
                    to_delete = head
                    prev = head
                else:
                    prev.next = to_delete.next
                    to_delete.next = None
                    to_delete = prev.next
            else:
                prev = to_delete
                to_delete = to_delete.next

        return head 