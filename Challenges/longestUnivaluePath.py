"""
Longest Univalue Path in Binary Tree

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

 

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

 

Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

 

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Intuition

We can think of any path (of nodes with the same values) as up to two arrows extending from it's root.

Specifically, the root of a path will be the unique node such that the parent of that node does not appear in the path, and an arrow will be a path where the root only has one child node in the path.

Then, for each node, we want to know what is the longest possible arrow extending left, and the longest possible arrow extending right? We can solve this using recursion.

Algorithm

Let arrow_length(node) be the length of the longest arrow that extends from the node. That will be 1 + arrow_length(node.left) if node.left exists and has the same value as node. Similarly for the node.right case.

While we are computing arrow lengths, each candidate answer will be the sum of the arrows in both directions from that node. We record these candidate answers and return the best one.

Time: O(N)
Space: O(H) where H is the height of our tree which is what the recursive call stack can be
"""
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.res = 0
        self.getPath(root)
        return self.res
    def getPath(self, node):
        if not node:
            return 0
        left = self.getPath(node.left)
        right = self.getPath(node.right)
        left_path_length, right_path_length = 0, 0
        if node.left and node.left.val == node.val:
            left_path_length = left + 1
        if node.right and node.right.val == node.val:
            right_path_length = right + 1
        self.res = max(self.res, left_path_length + right_path_length)
        return max(left_path_length, right_path_length)
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 0

        def longest(root):
            if not root:
                return 0
            leftPath = longest(root.left)
            rightPath = longest(root.right)
            left = (leftPath + 1) if root.left and root.val == root.left.val else 0
            right = (rightPath + 1) if root.right and root.val == root.right.val else 0
            self.longest = max(self.longest, left + right)
            return max(left, right)

        longest(root)
        return self.longest

