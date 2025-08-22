# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def count(self, head):
        temp = head
        count = 0

        while (temp != None):
            count += 1
            temp = temp.next
        
        return count
    
    def addNodes(self, head, d):
        temp = head

        while (temp.next != None):
            temp = temp.next
        
        for i in range(d):
            newNode = ListNode()
            temp.next = newNode
            temp = temp.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count1 = self.count(l1)
        count2 = self.count(l2)

        if (count1 >= count2):
            d = count1 - count2
            self.addNodes(l2, d)

        else:
            d = count2 - count1
            self.addNodes(l1, d)

        temp1 = l1
        temp2 = l2
        l3 = ListNode(-1)
        temp3 = l3
        sum1 = 0
        carry = 0

        while (temp1 != None and temp2 != None):
            sum1 = temp1.val + temp2.val + carry
            carry = 0

            carry = sum1 // 10
            sum1 = sum1 % 10

            newNode = ListNode(sum1)
            temp3.next = newNode
            temp3 = temp3.next

            temp1 = temp1.next
            temp2 = temp2.next

        if (carry >= 1):
            newNode = ListNode(carry)
            temp3.next = newNode
            temp3 = temp3.next
        
        l3 = l3.next

        return l3