# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root, ls):
        if (root == None):
            return
        
        self.inorder(root.left, ls)
        ls.append(root.val)
        self.inorder(root.right, ls)
    
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        ls = []

        self.inorder(root, ls)

        min1 = float("inf")

        for i in range(1, len(ls)):
            min1 = min(min1, ls[i] - ls[i - 1])
        
        return min1