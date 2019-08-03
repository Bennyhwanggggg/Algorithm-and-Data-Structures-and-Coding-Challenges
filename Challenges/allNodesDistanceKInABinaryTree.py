"""
All Nodes Distance K in Binary Tree

We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.

 

Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

Output: [7,4,1]

Explanation: 
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Intuition: Give a parent

If we know the parent of every node x, we know all nodes that are distance 1 from x. We can then perform a breadth first search from the target node to find the answer.

Algorithm

We first do a depth first search where we annotate every node with information about it's parent.

After, we do a breadth first search to find all nodes a distance K from the target.

Time: O(N)
Space: O(N)
"""
class Solution:
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        
        def dfs(node, parent=None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        
        queue = collections.deque([(target, 0)])
        seen = set([target])
        res = []
        while queue:
            node, dist = queue.popleft()
            if dist == K:
                res.append(node.val)
            
            for nei in [node.left, node.right, node.parent]:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, dist+1))
        
        return res

