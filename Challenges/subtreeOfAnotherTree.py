"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Naive approach, O(|s| * |t|)
For each node of s, let's check if it's subtree equals t. We can do that in a straightforward way by an isMatch function: check if s and t match at the values of their roots, plus their subtrees match. Then, in our main function, we want to check if s and t match, or if t is a subtree of a child of s.
"""
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        
        def isMatch(s, t):
            if not (s and t):
                return s is t
            return s.val == t.val and isMatch(s.left, t.left) and isMatch(s.right, t.right)
        
        if isMatch(s, t):
            return True
        if not s:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

