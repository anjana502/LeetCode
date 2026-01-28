/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int count(ListNode *head)
    {
        ListNode *temp = head;
        int p = 0;
        while (temp != NULL)
        {
            p++;
            temp = temp -> next;
        }
        return p;
    }
    
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int i, d;
        int count1 = count(headA);
        int count2 = count(headB);
        ListNode *cur1, *cur2;
        if (count1 >= count2)
        {
            d = count1 - count2;
            cur1 = headA;
            cur2 = headB;
        }
        else
        {
            d = count2 - count1;
            cur1 = headB;
            cur2 = headA;
        }
        for (i=0; i<d; i++)
        {
            cur1 = cur1 -> next;
        }
        
        while (cur1 != NULL && cur2 != NULL && cur1 != cur2)
        {
            cur1 = cur1 -> next;
            cur2 = cur2 -> next;
        }
        
        return cur1;
    }
};