"""
Binary Tree Right Side View
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Time Complexity O(N)
Space Complexity O(N)
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        left = ans + self.rightSideView(root.left)
        right = ans + self.rightSideView(root.right)
        if len(right) > len(left):
            return right
        return right + left[len(right):]
            
"""
BFS
"""
from collections import deque
class Solution:
    def rightSideView(self, root):
        if not root: 
            return []
        q, res = deque([root]), []
        while q:
            res.append(q[-1].val)
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return res

