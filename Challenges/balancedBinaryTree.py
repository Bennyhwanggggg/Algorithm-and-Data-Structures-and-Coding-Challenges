"""
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Recusive
Time: O(n log n) to traverse to depth of binary tree
Space: O(log n) depth of recursion (use memo to save time so we don't calculate same subtree)
"""
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def getHeight(self, root):
        if not root:
            return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))
    
"""
Memo
"""
class Solution(object):
    def __init__(self):
        self.d = {}
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def depth(root):
            if not root: return 0
            if(root in self.d): return self.d[root]
            self.d[root] = 1 + max(depth(root.left), depth(root.right))
            return self.d[root]
        if not root: return True
        return abs(depth(root.left) - depth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

