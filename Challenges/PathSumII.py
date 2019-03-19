# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        queue = collections.deque()
        queue.append(([root], [root.val], root.val)) # second list is not necessary if we just want to show node
        while queue:
            path, path_val, current_sum = queue.popleft()
            if not path[-1].left and not path[-1].right:
                if current_sum == sum:
                    result.append(path_val)
            if path[-1].left:
                newSum = current_sum+path[-1].left.val
                leftpath_val = path_val + [path[-1].left.val]
                leftpath = path + [path[-1].left]
                queue.append((leftpath, leftpath_val, newSum))
            if path[-1].right:
                newSum = current_sum+path[-1].right.val
                rightpath_val = path_val + [path[-1].right.val]
                rightpath = path + [path[-1].right]
                queue.append((rightpath, rightpath_val, newSum))
        return result
        