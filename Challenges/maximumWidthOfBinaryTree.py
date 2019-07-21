"""
Maximum Width of Binary Tree

Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:

Input: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:

Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:

Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:

Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
BFS

Traverse each node in breadth-first order, keeping track of that node's position. For each depth, the first node reached is the left-most, while the last node reached is the right-most.

Time Complexity: O(N) where NN is the number of nodes in the input tree. We traverse every node.

Space Complexity: O(N), the size of our queue.
"""
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = collections.deque([(root, 0, 0)])
        curr_depth = left = ans = 0
        while queue:
            node, depth, pos = queue.popleft()
            if node:
                queue.append((node.left, depth+1, pos*2))
                queue.append((node.right, depth+1, pos*2+1))
                if curr_depth != depth:  # when we start a new depth, keep track of it's pos
                    curr_depth = depth
                    left = pos
                ans = max(pos - left + 1, ans)
        return ans

