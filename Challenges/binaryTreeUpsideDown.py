"""
Binary Tree Upside Down

Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time: O(log(N))
Space: O(1)
"""
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # take care of the root
        left, right = root.left, root.right
        root.left, root.right = None, None
        
        # update the left and the right children, form the new tree, update root
        while left:
            newLeft, newRight = left.left, left.right
            left.left = right
            left.right = root
            root = left
            left = newLeft
            right = newRight
        return root

