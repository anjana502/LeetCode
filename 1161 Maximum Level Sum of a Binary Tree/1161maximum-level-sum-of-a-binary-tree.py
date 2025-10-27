from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        max1 = float("-inf")
        level = -1
        curr_level = 1

        while (len(q) != 0):
            d = len(q)
            sum1 = 0

            for i in range(d):
                node = q.popleft()
                sum1 += node.val

                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)
            
            if (sum1 > max1):
                max1 = sum1
                level = curr_level
            curr_level += 1
        
        return level