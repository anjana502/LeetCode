# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        head_odd = head
        head_even = head.next
        temp_odd = head_odd
        temp_even = head_even

        while (temp_even != None and temp_even.next != None):
            temp_odd.next = temp_even.next
            temp_even.next = temp_even.next.next
            temp_odd = temp_odd.next
            temp_even = temp_even.next
        
        temp_odd.next = head_even

        return head