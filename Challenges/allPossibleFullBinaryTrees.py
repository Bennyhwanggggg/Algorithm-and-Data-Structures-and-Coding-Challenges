"""
All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

 

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

 

Note:

1 <= N <= 20
"""
Note:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Intuition and Algorithm

Let FBT(N) be the list of all possible full binary trees with NN nodes.

Every full binary tree TT with 3 or more nodes, has 2 children at its root. Each of those children left and right are themselves full binary trees.

Thus, for N≥3, we can formulate the recursion: FBT(N)= [All trees with left child from FBT(x) and right child from FBT(N−1−x), for all x].

Also, by a simple counting argument, there are no full binary trees with a positive, even number of nodes.

Finally, we should cache previous results of the function FBT so that we don't have to recalculate them in our recursion.

Time: O(2^N)
Space: O(2^N)
"""
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        memo = {0: [], 1: [TreeNode(0)]} # base cases
        
        def generate(N):
            if N not in memo:
                ans = []
                for x in range(N): # the left subtree size
                    y = N - 1 - x # the right subtree size
                    for left in generate(x):
                        for right in generate(y):
                            bns = TreeNode(0)
                            bns.left = left
                            bns.right = right
                            ans.append(bns)
                memo[N] = ans
            return memo[N]
        
        generate(N)
        return memo[N]

