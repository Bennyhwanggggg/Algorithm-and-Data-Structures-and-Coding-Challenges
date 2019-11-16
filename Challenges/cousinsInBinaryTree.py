"""
Counsins In Binary Tree

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

 

Example 1:


Input: root = [1,2,3,4], x = 4, y = 3
Output: false
Example 2:


Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true
Example 3:



Input: root = [1,2,3,null,4], x = 2, y = 3
Output: false
 

Note:

The number of nodes in the tree will be between 2 and 100.
Each node has a unique integer value from 1 to 100.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Level order traversal
Time: O(N)
Space: O(d)
"""
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root or root.val == x or root.val == y:
            return False
        
        queue = collections.deque([root])
        
        while queue:
            temp = collections.deque()
            seen = set()
            while queue:
                node = queue.popleft()
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.left.val == y and node.right.val == x):
                        return False
                if node.left:
                    if node.left.val == x:
                        seen.add(x)
                    elif node.left.val == y:
                        seen.add(y)
                    temp.append(node.left)
                if node.right:
                    if node.right.val == x:
                        seen.add(x)
                    elif node.right.val == y:
                        seen.add(y)
                    temp.append(node.right)
            queue = temp
            if len(seen) == 2:
                return True
            elif len(seen) == 1:
                return False
        return False

