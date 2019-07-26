"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.res = []
        self.preorder(root, sum, [])
        return self.res
        
    def preorder(self, node, curr, path):
        if not node:
            return
        if not node.left and not node.right and curr == node.val:
                self.res.append(path + [node.val])
        else:
            if node.left:
                self.preorder(node.left, curr-node.val, path + [node.val])
            if node.right:
                self.preorder(node.right, curr-node.val, path + [node.val])
        
            
def pathSum(self, root, sum):
    if not root:
        return []
    res = []
    self.dfs(root, sum, [], res)
    return res
    
def dfs(self, root, sum, ls, res):
    if not root.left and not root.right and sum == root.val:
        ls.append(root.val)
        res.append(ls)
    if root.left:
        self.dfs(root.left, sum-root.val, ls+[root.val], res)
    if root.right:
        self.dfs(root.right, sum-root.val, ls+[root.val], res)
        
def pathSum2(self, root, sum):
    if not root:
        return []
    if not root.left and not root.right and sum == root.val:
        return [[root.val]]
    tmp = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
    return [[root.val]+i for i in tmp]




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


# DFS + stack I  
def pathSum4(self, root, sum): 
    if not root:
        return []
    res = []
    stack = [(root, sum-root.val, [root.val])]
    while stack:
        curr, val, ls = stack.pop()
        if not curr.left and not curr.right and val == 0:
            res.append(ls)
        if curr.right:
            stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
        if curr.left:
            stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
    return res 
        
