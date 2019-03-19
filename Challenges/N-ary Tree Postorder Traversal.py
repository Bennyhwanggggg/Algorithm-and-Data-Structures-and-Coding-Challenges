"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root):
            if not root:
                return
            for c in root.children:
                dfs(c)
            res.append(root.val)
        res = []
        dfs(root)
        return res