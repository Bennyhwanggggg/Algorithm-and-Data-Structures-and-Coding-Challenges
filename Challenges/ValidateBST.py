import sys


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBST(self, root, minV, maxV):
        if not root:
            return True
        if root.val > maxV or root.val < minV:
            return False
        return self.isBST(root.left, minV, root.val - 1) & self.isBST(root.right, root.val + 1, maxV)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        minV = -sys.maxsize
        maxV = sys.maxsize
        return self.isBST(root, minV, maxV)



