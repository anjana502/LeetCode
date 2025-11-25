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
    def connect(self, root: 'Node') -> 'Node':
        if (root == None):
            return root
        
        q = deque([])
        q.append(root)
        
        while (len(q) != 0):
            d = len(q)
            prev = None
            
            for i in range(d):
                curr = q.popleft()
                
                if (prev != None):
                    prev.next = curr
                
                prev = curr
                
                if (prev.left != None):
                    q.append(prev.left)
                if (prev.right != None):
                    q.append(prev.right)
        
        return root