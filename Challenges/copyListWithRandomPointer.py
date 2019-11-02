"""
Copy List With Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

 

Example 1:



Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
 

Note:

You must return the copy of the given head as a reference to the cloned list.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""

"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.seen = dict()
        
        def traverse(node):
            if node is None:
                return None
            if node in self.seen:  # if already seen, just use the cloned version
                return self.seen[node]
            
            # create a new node with the same value
            new_node = Node(node.val, None, None)
            
            self.seen[node] = new_node
            new_node.next = traverse(node.next)
            new_node.random = traverse(node.random)
            return new_node
        
        head = traverse(head)
        return head

