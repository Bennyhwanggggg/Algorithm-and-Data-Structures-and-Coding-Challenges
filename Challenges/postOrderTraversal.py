# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        
        def trav(root):
            if not root:
                return
            trav(root.left)
            trav(root.right)
            self.res.append(root.val)
        
        trav(root)
        return self.res
    
"""
Iterative
Preorder then reverse

Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NN is the number of nodes, i.e. the size of tree.

Space complexity : depending on the tree structure, we could keep up to the entire tree, therefore, the space complexity is O(N).
"""
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]

