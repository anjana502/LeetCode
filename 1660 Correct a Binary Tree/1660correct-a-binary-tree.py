from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, todelete):
        if (root == None):
            return
        
        if (root == todelete):
            return None
        
        root.left = self.deleteNode(root.left, todelete)
        root.right = self.deleteNode(root.right, todelete)
        
        return root
    
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        s = set()
        q.append(root)
        s.add(root.val)
        
        while (len(q) != 0):
            d = len(q)
            flag = False
            
            for i in range(d):
                node = q.popleft()
                
                if (node.left != None):
                    q.append(node.left)
                    s.add(node.left.val)
                if (node.right != None):
                    if (node.right.val in s):
                        todelete = node
                        flag = True
                        break
                    else:
                        q.append(node.right)
                        s.add(node.right.val)
            
            if (flag == True):
                break
        
        self.deleteNode(root, todelete)
        
        return root