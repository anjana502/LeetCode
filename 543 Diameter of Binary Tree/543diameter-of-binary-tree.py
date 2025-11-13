# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root, ls):
        if (root == None):
            return 0
        
        left = self.height(root.left, ls)
        right = self.height(root.right, ls)
        h = max(left, right) + 1

        ls[0] = max(ls[0], left + right)
        
        return h
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ls = [0]

        self.height(root, ls)

        return ls[0]