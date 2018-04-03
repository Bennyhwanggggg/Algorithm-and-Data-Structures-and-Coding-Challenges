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
        sorted_list = []
        
        for head in lists:
            current = head
            while current is not None:
                sorted_list.append(current)
                current = current.next
            
        sorted_list = sorted(sorted_list, key= lambda x: x.val)
        
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i+1]
            except:
                node.next = None
        
        if sorted_list:
            return sorted_list[0]
        else:
            return None