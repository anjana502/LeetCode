# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom1(self, root, level, ls):
        if (root == None):
            return
        
        if (len(ls) == level):
            ls.append([])
        
        ls[level].append(root.val)

        self.levelOrderBottom1(root.left, level + 1, ls)
        self.levelOrderBottom1(root.right, level + 1, ls)

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = []

        self.levelOrderBottom1(root, 0, ls)

        ls = ls[::-1]

        return ls