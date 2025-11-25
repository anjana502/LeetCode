# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal1(self, root, ls):
        if (root == None):
            return
        
        self.postorderTraversal1(root.left, ls)
        self.postorderTraversal1(root.right, ls)
        ls.append(root.val)
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        
        self.postorderTraversal1(root, ls)
        
        return ls