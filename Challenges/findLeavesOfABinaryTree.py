"""
Find Leaves Of A Binary Tree

Given a binary tree, collect a tree's nodes as if you were doing this: Collect and remove all leaves, repeat until the tree is empty.

 

Example:

Input: [1,2,3,4,5]
  
          1
         / \
        2   3
       / \     
      4   5    

Output: [[4,5,3],[2],[1]]
 

Explanation:

1. Removing the leaves [4,5,3] would result in this tree:

          1
         / 
        2          
 

2. Now removing the leaf [2] would result in this tree:

          1          
 

3. Now removing the leaf [1] would result in the empty tree:

          []  
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
DFS
Each leaves level will have same height so use that to store the results
Time: O(N)
Space: O(N)
"""
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []
        def dfs(root):
            if not root:
                return -1
            height = max(dfs(root.left), dfs(root.right)) + 1
            if height >= len(res):
                res.append([])
            res[height].append(root.val)
            return height
        dfs(root)
        return res
        

