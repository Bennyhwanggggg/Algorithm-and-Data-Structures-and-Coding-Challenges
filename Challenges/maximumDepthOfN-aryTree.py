"""
Maximum Depth of N-ary Tree
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

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
Time and Space: O(N)
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        ans = 1
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            ans = max(ans, level)
            for child in node.children:
                if child is not None:
                    queue.append((child, level+1))
        return ans

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        return max([self.maxDepth(child) for child in root.children] + [0]) + 1 if root else 0
