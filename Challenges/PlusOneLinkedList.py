# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        stack = []
        current = head
        while current:
            stack.append(current)
            current = current.next
        carry = 0
        while stack:
            node = stack.pop()
            node.val += 1
            if node.val == 10:
                carry = 1
            else:
                carry = 0
            if carry:
                node.val = 0
            else:
                break

        if carry:
            first = ListNode(1)
            first.next = head
            head = first
        return head
