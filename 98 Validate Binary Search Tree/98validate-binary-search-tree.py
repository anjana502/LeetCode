# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST1(self, root, min1, max1):
        if (root == None):
            return True
        
        if (root.val <= min1 or root.val >= max1):
            return False
        
        return (self.isValidBST1(root.left, min1, root.val) and self.isValidBST1(root.right, root.val, max1))
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBST1(root, float("-inf"), float("inf"))