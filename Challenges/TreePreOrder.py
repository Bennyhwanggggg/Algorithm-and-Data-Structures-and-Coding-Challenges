# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        path = []
        
        def preOrder(root):
            if not root:
                return
            path.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        
        preOrder(root)
        return path