# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        order = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            order.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return order[k - 1]
