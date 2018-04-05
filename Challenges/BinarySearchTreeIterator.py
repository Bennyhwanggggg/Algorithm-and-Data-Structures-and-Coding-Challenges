# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.curr = root

    def hasNext(self):
        """
        :rtype: bool
        """
        return True if self.stack or self.curr else False

    def next(self):
        """
        :rtype: int
        """
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left

        self.curr = self.stack.pop()
        val = self.curr.val
        self.curr = self.curr.right
        return val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())