# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        if (root == None):
            return [0, 0]
        
        left_rob, left_not = self.dfs(root.left)
        right_rob, right_not = self.dfs(root.right)

        root_rob = root.val + left_not + right_not
        root_not = max(left_rob, left_not) + max(right_rob, right_not)

        return [root_rob, root_not]
    
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.dfs(root))