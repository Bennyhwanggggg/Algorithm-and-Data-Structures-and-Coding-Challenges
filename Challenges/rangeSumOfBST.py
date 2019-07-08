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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        def dfs(node):
            if not node:
                return 0
            if L <= node.val and node.val <= R:
                self.ans += node.val
            if node.val > L:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)
        
        self.ans = 0
        dfs(root)
        return self.ans
