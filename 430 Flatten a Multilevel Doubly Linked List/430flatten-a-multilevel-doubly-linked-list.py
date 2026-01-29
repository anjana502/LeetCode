"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if (head == None):
            return head
        
        temp = head

        while (temp.next != None):
            temp = temp.next
        
        while (temp != None):
            if (temp.child != None):
                head1 = self.flatten(temp.child)
                
                temp1 = head1

                while (temp1.next != None):
                    temp1 = temp1.next
                
                next1 = temp.next
                temp.next = head1
                temp1.next = next1
                head1.prev = temp

                if (next1 != None):
                    next1.prev = temp1
                
                temp.child = None
            
            temp = temp.prev
        
        return head