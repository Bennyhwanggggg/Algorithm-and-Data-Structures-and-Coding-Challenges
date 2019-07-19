"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
The pseudocode is as following:

Initialize current node to dummy head of the returning list.
Initialize carry to 00.
Initialize pp and qq to head of l1l1 and l2l2 respectively.
Loop through lists l1l1 and l2l2 until you reach both ends.
Set xx to node pp's value. If pp has reached the end of l1l1, set to 00.
Set yy to node qq's value. If qq has reached the end of l2l2, set to 00.
Set sum = x + y + carry.
Update carry = sum/10.
Create a new node with the digit value of (summod10) and set it to current node's next, then advance current node to next.
Advance both pp and qq.
Check if carry = 1, if so append a new node with digit 11 to the returning list.
Return dummy head's next node.

Time complexity : O(max(m,n)). Assume that mm and nn represents the length of l1l1 and l2l2 respectively, the algorithm above iterates at most max(m,n) times.

Space complexity : O(max(m,n)). The length of the new list is at most max(m,n)+1.
"""

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        
        val = l1.val + l2.val + c
        c = val //10
        ret = ListNode(val%10)
        if l1.next != None or l2.next != None or c!= 0:
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret
                
"""
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    ListNode dummyHead = new ListNode(0);
    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;
    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;
        carry = sum / 10;
        curr.next = new ListNode(sum % 10);
        curr = curr.next;
        if (p != null) p = p.next;
        if (q != null) q = q.next;
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = ListNode(0)
        dummy = temp
        carry = 0
        while l1 and l2:
            new = l1.val + l2.val + carry
            if new >= 10:
                carry = 1
                new = new % 10
            else:
                carry = 0
            newNode = ListNode(new)
            temp.next = newNode
            temp = temp.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            new = l1.val + carry
            if new >= 10:
                carry = 1
                new = new % 10
            else:
                carry = 0
            newNode = ListNode(new)
            temp.next = newNode
            temp = temp.next
            l1 = l1.next

        while l2:
            new = l2.val + carry
            if new >= 10:
                carry = 1
                new = new % 10
            else:
                carry = 0
            newNode = ListNode(new)
            temp.next = newNode
            temp = temp.next
            l2 = l2.next

        if carry:
            newNode = ListNode(1)
            temp.next = newNode

        return dummy.next


