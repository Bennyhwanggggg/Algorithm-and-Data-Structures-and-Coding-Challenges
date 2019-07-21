"""
Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Top Down DFS
Time: O(n) traverse n nodes
Space: O(n) recursion stack space
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, parent, length):
            if not node:
                return
            length = length + 1 if parent.val + 1 == node.val else 1
            self.res = max(self.res, length)
            dfs(node.left, node, length)
            dfs(node.right, node, length)
        
        dfs(root, root, 0)
        return self.res

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return self.res
        self.getPath(root, root.val, 1)
        return self.res
    
    def getPath(self, node, parentVal, length):
        if not node:
            self.res = max(self.res, length)
            return
        if node.val == parentVal + 1:
            length += 1
            self.res = max(self.res, length)
            self.getPath(node.left, node.val, length)
            self.getPath(node.right, node.val, length)
        else:
            self.getPath(node.left, node.val, 1)
            self.getPath(node.right, node.val, 1)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max_consec = 0
        self.helper(root, self.max_consec, root.val + 1)
        return self.max_consec

    def helper(self, root, consec, target):
        if not root:
            return
        if root.val == target:
            consec += 1
        else:
            consec = 1
        self.max_consec = max(self.max_consec, consec)
        self.helper(root.right, consec, root.val + 1)
        self.helper(root.left, consec, root.val + 1)


