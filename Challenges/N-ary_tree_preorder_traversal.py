"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                dfs(child)
        dfs(root)
        return res

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.result = []
        self.traverse(root)
        return self.result
    
    def traverse(self, node):
        if not node:
            return
        self.result.append(node.val)
        for child in node.children:
            self.traverse(child)
