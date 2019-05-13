# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        res = 0
        stack = [root]
        while stack:
            curr = stack.pop()
            if curr is not None:
                if L <= curr.val <= R:
                    res += curr.val
                if L < curr.val:
                    stack.append(curr.left)
                if curr.val < R:
                    stack.append(curr.right)
        return res
