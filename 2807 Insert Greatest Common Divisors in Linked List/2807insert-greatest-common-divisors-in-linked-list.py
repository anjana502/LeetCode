# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        if (b == 0):
            return a
        
        return self.gcd(b, a % b)
    
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        temp = head

        while (temp != None and temp.next != None):
            result = self.gcd(temp.val, temp.next.val)
            next1 = temp.next
            newNode = ListNode(result)
            temp.next = newNode
            newNode.next = next1
            temp = next1
        
        return head