# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_depth = 0
        self.deep(root, 1)
        return self.max_depth
        
    def deep(self, root, depth):
        if not root:
            return
        self.max_depth = max(self.max_depth, depth)
        self.deep(root.left, depth + 1)
        self.deep(root.right, depth + 1)
    