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


