# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfNodes(self, root):
        if (root == None):
            return 0
        
        left = self.sumOfNodes(root.left)
        right = self.sumOfNodes(root.right)

        sum1 = root.val + left + right

        return sum1
    
    def maxProduct1(self, root, total_sum, ls):
        if (root == None):
            return 0
        
        left = self.maxProduct1(root.left, total_sum, ls)
        right = self.maxProduct1(root.right, total_sum, ls)

        p1 = left * (total_sum - left)
        p2 = right * (total_sum - right)

        max1 = max(p1, p2)
        ls[0] = max(ls[0], max1)
        
        sum1 = root.val + left + right

        return sum1

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = self.sumOfNodes(root)
        ls = [float("-inf")]

        self.maxProduct1(root, total_sum, ls)

        ls[0] %= (10 ** 9 + 7)
        
        return ls[0]