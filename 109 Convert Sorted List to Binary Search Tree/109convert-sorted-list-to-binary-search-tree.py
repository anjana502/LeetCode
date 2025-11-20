# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if (head == None):
            return head
        if (head.next == None):
            root = TreeNode(head.val)
            return root
        
        prev = head
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None
        head1 = slow.next
        slow.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(head1)

        return root