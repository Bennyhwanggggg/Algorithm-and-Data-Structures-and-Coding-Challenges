"""
Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Time: O(N)
Space: O(N) where N are number of nodes
"""
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        queue = collections.deque([(root, 1)])
        levels = collections.defaultdict(list)
        # odd number level is left to right and even number is right to left
        while queue:
            node, level = queue.popleft()
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        for lv in sorted(levels.keys()):
            if lv%2:
                result.append(levels[lv])
            else:
                result.append(levels[lv][::-1])
        return result
                
