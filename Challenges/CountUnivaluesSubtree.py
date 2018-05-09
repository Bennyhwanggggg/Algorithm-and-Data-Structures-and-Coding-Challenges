# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0
        self.helper(root)
        return self.result

    def helper(self, root):
        if not root:
            return True
        left = self.helper(root.left)
        right = self.helper(root.right)
        if left and right:
            if root.left and root.val != root.left.val:
                return False
            if root.right and root.val != root.right.val:
                return False
            self.result += 1
            return True
        return False
