# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """



        self.trav = []

        self.preOrder(root)
        mindiff = float('inf')
        print(self.trav)
        for i in range(1, len(self.trav)):
            mindiff = min(self.trav[i] - self.trav[i - 1], mindiff)
        return mindiff

    def preOrder(self, root):
        if not root:
            return
        self.preOrder(root.left)
        self.trav.append(root.val)
        self.preOrder(root.right)
        return