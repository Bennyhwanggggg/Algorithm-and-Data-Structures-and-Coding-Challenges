"""
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            if prev and curr.val == prev.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return head

