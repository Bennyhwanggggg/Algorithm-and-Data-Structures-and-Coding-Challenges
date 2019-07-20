"""
Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Recursion

Time: O(N)
Space: O(N)
"""
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        def helper(root, left, right):
            if not root:
                return True
            if root.val < left or root.val > right:
                return False
            return helper(root.left, left, root.val-1) and helper(root.right, root.val+1, right)
        
        return helper(root, -float('inf'), float('inf'))
    
"""
Iterative
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True  

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



