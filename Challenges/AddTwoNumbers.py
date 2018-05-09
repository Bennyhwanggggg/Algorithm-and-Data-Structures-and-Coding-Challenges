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
