# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        return_list = []

        for head in lists:
            current = head
            while current:
                return_list.append(current)
                current = current.next

        return_list = sorted(return_list, key=lambda x: x.val)

        for i, node in enumerate(return_list):
            try:
                node.next = return_list[i + 1]
            except:
                node.next = None

        return return_list[0] if return_list else None


# Python2
from Queue import PriorityQueue


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = point = ListNode(0)
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, node))

        while not pq.empty():
            val, node = pq.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                pq.put((node.val, node))
        return head.next


# python 3
# Time: O(Nlog(K)
# Space: O(N)
# Put all current pointers into pq and keep popping the smallest one and add its next to pq
from queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = point = ListNode(0)
        count = 0
        pq = PriorityQueue()
        for node in lists:
            if node:
                pq.put((node.val, count, node))
                count += 1
        
        while not pq.empty():
            val, _, node = pq.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                pq.put((node.val, count, node))
                count += 1
        
        return dummy.next

