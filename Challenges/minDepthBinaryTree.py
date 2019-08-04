# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = [(root, 1)]
        while queue:
            node, level = queue.pop(0)
            if not node.left and not node.right:
                return level
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))

"""
Recursive

Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NN is the number of nodes.
Space: O(N) if unbalanced tree
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1
        
        min_depth = float('inf')
        for c in [root.left, root.right]:
            if c:
                min_depth = min(min_depth, self.minDepth(c))
        return min_depth+1
