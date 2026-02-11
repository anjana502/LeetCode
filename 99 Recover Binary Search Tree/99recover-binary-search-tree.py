# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def in_order(self, root, ls1):
        if (root == None):
            return
        
        self.in_order(root.left, ls1)
        ls1.append(root)
        self.in_order(root.right, ls1)
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        ls1 = []

        self.in_order(root, ls1)

        ls = sorted(ls1, key = lambda i: i.val)

        for i in range(len(ls1)):
            if (ls[i].val != ls1[i].val):
                j = ls.index(ls1[i])
                break

        ls1[i].val, ls1[j].val = ls1[j].val, ls1[i].val