from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if (root == None):
            return root
        
        q = deque([])
        q.append(root)
        
        while (len(q) != 0):
            d = len(q)
            prev = q.popleft()
            
            if (prev.left != None):
                q.append(prev.left)
            if (prev.right != None):
                q.append(prev.right)
            
            for i in range(d - 1):
                curr = q.popleft()
                
                if (curr.left != None):
                    q.append(curr.left)
                if (curr.right != None):
                    q.append(curr.right)
                
                prev.next = curr
                prev = curr
        
        return root
                