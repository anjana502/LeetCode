# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ls = []
        self.inOrder(root)
        self.index = -1

    def next(self) -> int:
        self.index += 1
        return self.ls[self.index]

    def hasNext(self) -> bool:
        if (self.index + 1 < len(self.ls)):
            return True
        return False

    def inOrder(self, root):
        if (root == None):
            return
        
        self.inOrder(root.left)
        self.ls.append(root.val)
        self.inOrder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()