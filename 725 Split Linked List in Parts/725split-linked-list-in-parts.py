# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ls = [None for i in range(k)]

        if (head == None):
            return ls
        
        count = 0
        temp = head

        while (temp != None):
            count += 1
            temp = temp.next
        
        n1 = count % k
        d1 = (count // k) + 1
        temp = head
        prev = head

        for i in range(n1):
            ls[i] = temp
            j = 0

            while (temp != None and j < d1):
                prev = temp
                temp = temp.next
                j += 1
                
            prev.next = None
        
        n2 = k - n1
        d2 = (count // k)

        for i in range(n1, k):
            ls[i] = temp
            j = 0

            while (temp != None and j < d2):
                prev = temp
                temp = temp.next
                j += 1
                
            prev.next = None
        
        return ls