# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        if not root:
            return []
        currLv = 1
        queue.append((root, currLv))
        hights = {}
        while queue:
            node, currLv = queue.popleft()
            if currLv not in hights:
                hights[currLv] = [node.val]
            else:
                hights[currLv].append(node.val)
            currLv += 1
            if node.left:
                queue.append((node.left, currLv))
            if node.right:
                queue.append((node.right, currLv))

        return [lv for lv in hights.values()]