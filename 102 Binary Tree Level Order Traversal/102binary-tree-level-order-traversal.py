from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = []

        if (root == None):
            return ls

        q = deque([])
        q.append(root)

        while (len(q) != 0):
            d = len(q)
            ls1 = []

            for i in range(d):
                d1 = q.popleft()
                ls1.append(d1.val)

                if (d1.left != None):
                    q.append(d1.left)
                if (d1.right != None):
                    q.append(d1.right)

            ls.append(ls1)

        return ls        