"""
Reverse Linked List In between two nodes

Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Iterative
Time: O(N)
Space: O(1)
"""
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        
        # move the two pointers until they reach the proper starting point
        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m -= 1
            n -= 1
        
        tail, concat = curr, prev
        
        # reverse up to n
        while n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            n -= 1
        
        if concat:
            concat.next = prev
        else:
            head = prev
        tail.next = curr
        return head

