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
