"""
Given a complete binary tree, count the number of nodes.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
If you draw the tree out with at least 4 levels (the root is considered a level), you'll notice that either the left or right subtree of the current node you're on will be a PERFECT subtree.

Since you know this, you can compare the left and bottom most node of each subtree to see if they are the same depth. If they are the same depth, you can add the number of nodes in the left subtree (2**left subtree height - 1) + 1 (the current node you're on) + the nodes in the rightsubtree (recurse function for countNodes).

If the two heights of your left tree and right tree are NOT the same, then then you know the right subtree is perfect and you can start counting the nodes in your left subtree instead.

The base case is when you reach a null node.

It's always hard to imagine the entire recursion call stack in your head, so I would suggest you draw out a the cases, then convince yourself they will work all the way down to the base case. Otherwise you will get conufused.
"""
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def depth(root):
            if not root: 
                return 0 
            return 1 + depth(root.left)

        
        if not root: 
            return 0
        lh = depth(root.left)
        rh = depth(root.right)
        if lh == rh: 
            return 1 + (2**lh - 1) + self.countNodes(root.right)
        else: 
            return 1 + (2**rh - 1) + self.countNodes(root.left) 
