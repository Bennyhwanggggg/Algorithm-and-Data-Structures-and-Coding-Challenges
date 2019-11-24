"""
Insufficient Nodes in Root to Leafs Paths

Given the root of a binary tree, consider all root to leaf paths: paths from the root to any leaf.  (A leaf is a node with no children.)

A node is insufficient if every such root to leaf path intersecting this node has sum strictly less than limit.

Delete all insufficient nodes simultaneously, and return the root of the resulting binary tree.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1

Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22

Output: [5,4,8,11,null,17,4,7,null,null,null,5]
 

Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1

Output: [1,null,-3,4]
 

Note:

The given tree will have between 1 and 5000 nodes.
-10^5 <= node.val <= 10^5
-10^9 <= limit <= 10^9
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Intuition
If root is leaf,
we compare the limit and root.val,
and return the result directly.

If root is leaf,
we recursively call the function on root's children with limit = limit - root.val.

Note that if a node become a new leaf,
it means it has no valid path leading to an original leaf,
we need to remove it.

Explanation
if root.left == root.right == null, root is leaf with no child {
    if root.val < limit, we return null;
    else we return root.
}
if root.left != null, root has left child {
    Recursively call sufficientSubset function on left child,
    with limit = limit - root.val
}
if root.right != null, root has right child {
    Recursively call sufficientSubset function on right child,
    with limit = limit - root.val
}
if root.left == root.right == null,
root has no more children, no valid path left,
we return null;
else we return root.

Complexity
Time O(N)
Space O(height) for recursion management.

"""
class Solution:
    def sufficientSubset(self, root: TreeNode, limit: int) -> TreeNode:
        if not root.left and not root.right:
            return None if root.val < limit else root
        if root.left:
            root.left = self.sufficientSubset(root.left, limit - root.val)
        if root.right:
            root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None

