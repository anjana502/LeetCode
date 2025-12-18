from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ls = []

        if (root == None):
            return ls
        
        q = deque([])
        q.append(root)
        flag = True

        while (len(q) != 0):
            d = len(q)
            ls1 = []

            for i in range(d):
                if (flag == True):
                    d1 = q.popleft()
                    ls1.append(d1.val)

                    if (d1.left != None):
                        q.append(d1.left)
                    if (d1.right != None):
                        q.append(d1.right)
                else:
                    d1 = q.pop()
                    ls1.append(d1.val)

                    if (d1.right != None):
                        q.appendleft(d1.right)
                    if (d1.left != None):
                        q.appendleft(d1.left)
            
            ls.append(ls1)
            flag = False if (flag == True) else True
        
        return ls