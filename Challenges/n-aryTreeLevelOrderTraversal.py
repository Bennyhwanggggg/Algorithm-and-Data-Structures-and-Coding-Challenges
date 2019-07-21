"""
N-ary Tree Level Order Traversal

Given an n-ary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
 
We should return its level order traversal:

[
     [1],
     [3,2,4],
     [5,6]
]
 

Note:

The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = collections.deque([root])
        while queue:
            res.append([node.val for node in queue])
            new_level = []
            while queue:
                node = queue.popleft()
                new_level.extend(node.children)
            queue = collections.deque(new_level)
        return res
            
