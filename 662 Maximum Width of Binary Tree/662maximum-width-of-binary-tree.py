from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))
        max1 = -1

        while (len(q) != 0):
            d = len(q)
            max1 = max(max1, q[-1][1] - q[0][1] + 1)

            for j in range(d):
                node, index = q.popleft()

                if (node.left != None):
                    q.append((node.left, 2 * index + 1))
                if (node.right != None):
                    q.append((node.right, 2 * index + 2))
        
        return max1