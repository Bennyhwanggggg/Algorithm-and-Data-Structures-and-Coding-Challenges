"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        stack = collections.deque([root])
        while stack:
            res = []
            for node in stack:
                res.append(node.val)
            result.append(res)
            new_level = []
            while stack:
                curr = stack.popleft()
                if curr.left:
                    new_level.append(curr.left)
                if curr.right:
                    new_level.append(curr.right)
            stack = collections.deque(new_level)
        return result
    
from collections import deque
"""
Iterative
Time: O(N)
Space: O(N)
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return levels
    
"""
Recursive
Time: O(N)
Space: O(N)
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)
            
        helper(root, 0)
        return levels
    

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
