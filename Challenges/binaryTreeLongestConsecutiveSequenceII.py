"""
Binary Tree Longest Consecutive Sequence II

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
This solution is very simple. With every node, we associate two values/variables named inrinr and dcrdcr, where incrincr represents the length of the longest incrementing branch below the current node including itself, and dcrdcr represents the length of the longest decrementing branch below the current node including itself.

We make use of a recursive function longestPath(node) which returns an array of the form [inr,dcr] for the calling node. We start off by assigning both inrinr and dcrdcr as 1 for the current node. This is because the node itself always forms a consecutive increasing as well as decreasing path of length 1.

Then, we obtain the length of the longest path for the left child of the current node using longestPath[root.left]. Now, if the left child is just smaller than the current node, it forms a decreasing sequence with the current node. Thus, the dcrdcr value for the current node is stored as the left child's dcrdcr value + 1. But, if the left child is just larger than the current node, it forms an incrementing sequence with the current node. Thus, we update the current node's inrinr value as left_child(inr)+1.

Then, we do the same process with the right child as well. But, for obtaining the inrinr and dcrdcr value for the current node, we need to consider the maximum value out of the two values obtained from the left and the right child for both inrinr and dcrdcr, since we need to consider the longest sequence possible.

Further, after we've obtained the final updated values of inrinr and dcrdcr for a node, we update the length of the longest consecutive path found so far as maxval=max(inr+dcr−1).
"""
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
        self.res = 0
        
        def dfs(node, parent):
            if not node:
                return 0, 0
            left_inc, left_dec = dfs(node.left, node)
            right_inc, right_dec = dfs(node.right, node)
            self.res = max(self.res, left_inc + right_dec + 1, left_dec + right_inc + 1)
            if node.val == parent.val + 1:
                return max(left_inc, right_inc) + 1, 0
            if node.val == parent.val - 1:
                return 0, max(left_dec, right_dec) + 1
            return 0, 0
        dfs(root, root)
        return self.res

