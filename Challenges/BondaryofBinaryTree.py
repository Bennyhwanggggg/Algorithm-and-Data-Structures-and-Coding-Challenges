# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.boundary = [root]
        self.leftbound(root.left)
        self.leafbound(root)
        self.rightbound(root.right)
        return [node.val for node in self.boundary]

    def leftbound(self, root):
        if not root:
            return
        if root not in self.boundary:
            self.boundary.append(root)
            if root.left:
                self.leftbound(root.left)
            else:
                self.leftbound(root.right)
        return

    def rightbound(self, root):
        if not root:
            return
        if root.right:
            self.rightbound(root.right)
        else:
            self.rightbound(root.left)
        if root not in self.boundary:
            self.boundary.append(root)
        return

    def leafbound(self, root):
        if not root:
            return
        if not root.left and not root.right and root not in self.boundary:
            self.boundary.append(root)
        self.leafbound(root.left)
        self.leafbound(root.right)
        return


class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []

        left_bd_nodes = [root]
        cur = root.left
        while cur:
            left_bd_nodes.append(cur)
            cur = cur.left or cur.right

        right_bd_nodes = [root]
        cur = root.right
        while cur:
            right_bd_nodes.append(cur)
            cur = cur.right or cur.left

        leaf_nodes = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            if not node.left and not node.right:
                leaf_nodes.append(node)

        ans = []
        seen = set()
        def visit(node):
            if node not in seen:
                seen.add(node)
                ans.append(node.val)

        for node in left_bd_nodes: visit(node)
        for node in leaf_nodes: visit(node)
        for node in reversed(right_bd_nodes): visit(node)

        return ans