# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftHeight(self, root):
        h = 0
        
        while (root != None):
            h += 1
            root = root.left
        
        return h
    
    def rightHeight(self, root):
        h = 0
        
        while (root != None):
            h += 1
            root = root.right
        
        return h
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        
        left = self.leftHeight(root)
        right = self.rightHeight(root)
        
        if (left == right):
            return ((1 << left) - 1)
        
        return (1 + self.countNodes(root.left) + self.countNodes(root.right))