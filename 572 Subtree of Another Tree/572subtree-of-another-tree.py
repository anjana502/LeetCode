# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree1(self, root1, root2):
        if (root1 == None and root2 == None):
            return True
        if (root1 == None or root2 == None):
            return False
        
        if (root1.val != root2.val):
            return False
        
        return (self.isSubtree1(root1.left, root2.left) and self.isSubtree1(root1.right, root2.right))
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (subRoot == None):
            return True
        if (root == None):
            return False
        
        if (root.val == subRoot.val):
            if (self.isSubtree1(root, subRoot) == True):
                return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))