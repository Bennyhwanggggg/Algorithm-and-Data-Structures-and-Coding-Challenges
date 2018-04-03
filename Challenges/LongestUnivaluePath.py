# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def longest(root):
            if not root:
                return 0
            leftPath = longest(root.left)
            rightPath = longest(root.right)
            left = (leftPath + 1) if root.left and root.val == root.left.val else 0
            right = (rightPath + 1) if root.right and root.val == root.right.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)

        longest(root)
        return self.longest

