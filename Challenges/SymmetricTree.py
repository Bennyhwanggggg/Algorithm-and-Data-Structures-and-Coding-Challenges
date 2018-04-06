# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.mirror(root.left, root.right)
    
    def mirror(self, leftroot, rightroot):
        if not leftroot and not rightroot:
            return True
        if not leftroot or not rightroot:
            return False
        if leftroot.val != rightroot.val:
            return False
        return self.mirror(leftroot.right, rightroot.left) and self.mirror(leftroot.left, rightroot.right)
        