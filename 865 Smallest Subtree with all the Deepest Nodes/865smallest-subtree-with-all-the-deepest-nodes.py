from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mapParentNodes(self, root, parent, d):
        if (root == None):
            return
        
        d[root] = parent

        self.mapParentNodes(root.left, root, d)
        self.mapParentNodes(root.right, root, d)
    
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque([])
        d = {}

        self.mapParentNodes(root, None, d)

        q.append(root)
        ls = []

        while (len(q) != 0):
            ls = []
            d1 = len(q)

            for i in range(d1):
                node = q.popleft()
                ls.append(node)

                if (node.left != None):
                    q.append(node.left)
                if (node.right != None):
                    q.append(node.right)
        
        q = deque(ls)
        s = set()
        
        while (len(q) > 1):
            node = q.popleft()
            d1 = d[node].val

            if (d1 not in s):
                q.append(d[node])
                s.add(d1)

        return q[0]