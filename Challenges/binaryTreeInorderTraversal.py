# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        visited = []

        def inOrder(root):
            if not root:
                return

            inOrder(root.left)
            visited.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return visited


