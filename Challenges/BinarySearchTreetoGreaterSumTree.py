"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Method 1:
Iterative version: use stack to pop out the nodes in reversed in order sequence.

Initially, use cur to point to the root,
1. push into Stack the right-most path of current subtree;
2. pop out a node, update sum and the node value;
3. point cur to the node's left child, if any;
4. Repeat the above till the stack is empty and cur has no left child.

Analysis:
Time & space: O(n).

Method 2:
Recursive version: using a sum TreeNode (more safety) instead of an instance variable.
Obviously, sum updates its value by reversed in-order traversal of nodes.

Analysis:
Time: O(n), space: O(n) if considering recursion stack.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        res = root
        sumSoFar = 0
        while root is not None or len(stack):
            while root is not None:
                stack.append(root)
                root = root.right
            node = stack.pop()
            sumSoFar += node.val
            node.val = sumSoFar
            root = node.left
        return res
