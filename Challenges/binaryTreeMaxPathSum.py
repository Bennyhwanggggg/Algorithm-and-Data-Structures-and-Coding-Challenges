"""
Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Algorithm

Now everything is ready to write down an algorithm.

Initiate max_sum as the smallest possible integer and call max_gain(node = root).
Implement max_gain(node) with a check to continue the old path/to start a new path:
Base case : if node is null, the max gain is 0.
Call max_gain recursively for the node children to compute max gain from the left and right subtrees : left_gain = max(max_gain(node.left), 0) and
right_gain = max(max_gain(node.right), 0).
Now check to continue the old path or to start a new path. To start a new path would cost price_newpath = node.val + left_gain + right_gain. Update max_sum if it's better to start a new path.
For the recursion return the max gain the node and one/zero of its subtrees could add to the current path : node.val + max(left_gain, right_gain).

Time: O(N)
Space: O(log(N)) which is the recusion stack of size of tree's height
"""
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = -float('inf')
        def max_gain(node):
            if not node:
                return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            price_newpath = node.val + left_gain + right_gain
            
            self.max_sum = max(self.max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum

