# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder1(self, preorder, ls, min1, max1):
        if (ls[0] >= len(preorder)):
            return None
        
        data = preorder[ls[0]]

        if (data <= min1 or data >= max1):
            return None
        
        root = TreeNode(data)
        ls[0] += 1

        root.left = self.bstFromPreorder1(preorder, ls, min1, data)
        root.right = self.bstFromPreorder1(preorder, ls, data, max1)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        ls = [0]
        return self.bstFromPreorder1(preorder, ls, float("-inf"), float("inf"))