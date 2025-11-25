# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree1(self, postorder, inorder, ls, d, low, high):
        if (low > high):
            return None
        
        data = postorder[ls[0]]
        root = TreeNode(data)
        index = d[data]
        ls[0] -= 1
        
        root.right = self.buildTree1(postorder, inorder, ls, d, index + 1, high)
        root.left = self.buildTree1(postorder, inorder, ls, d, low, index - 1)
        
        return root
    
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        d = {inorder[i]: i for i in range(len(inorder))}
        ls = [len(inorder) - 1]
        
        return self.buildTree1(postorder, inorder, ls, d, 0, len(inorder) - 1)