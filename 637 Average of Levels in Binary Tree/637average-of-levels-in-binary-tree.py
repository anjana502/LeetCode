# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, level, root, ls, count):
        if (root == None):
            return
        
        if (level == len(ls)):
            ls.append([0])
            count.append([0])
        
        ls[level][0] += (root.val)
        count[level][0] += 1

        self.dfs(level + 1, root.left, ls, count)
        self.dfs(level + 1, root.right, ls, count)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ls = []
        count = []

        self.dfs(0, root, ls, count)

        for i in range(len(ls)):
            ls[i][0] /= count[i][0]
        
        ls = [i[0] for i in ls]
        
        return ls