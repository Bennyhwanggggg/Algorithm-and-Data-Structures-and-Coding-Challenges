# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            path.append(root.val)
            
        postOrder(root)
        return path