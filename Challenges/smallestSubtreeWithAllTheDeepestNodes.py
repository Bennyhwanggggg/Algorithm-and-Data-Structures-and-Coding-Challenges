"""
Smallest Subtree with all the Deepest Nodes

Given a binary tree rooted at root, the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is that node, plus the set of all descendants of that node.

Return the node with the largest depth such that it contains all the deepest nodes in its subtree.

 

Example 1:

Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]
Explanation:



We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the given tree.
The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with value 2.
Both the input and output have TreeNode type.
 

Note:

The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
DFS

We try a straightforward approach that has two phases.

The first phase is to identify the nodes of the tree that are deepest. To do this, we have to annotate the depth of each node. We can do this with a depth first search.

Afterwards, we will use that annotation to help us find the answer:

If the node in question has maximum depth, it is the answer.

If both the left and right child of a node have a deepest descendant, then the answer is this parent node.

Otherwise, if some child has a deepest descendant, then the answer is that child.

Otherwise, the answer for this subtree doesn't exist.

Algorithm

In the first phase, we use a depth first search dfs to annotate our nodes.

In the second phase, we also use a depth first search answer(node), returning the answer for the subtree at that node, and using the rules above to build our answer from the answers of the children of node.

Note that in this approach, the answer function returns answers that have the deepest nodes of the entire tree, not just the subtree being considered.

Time: O(N)
Space: O(N)
"""
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        lmd = rmd = root  # left and right most deepest node
        queue = collections.deque([(root, 0)])  # BFS with depth
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            if depth > max_depth:
                max_depth = depth
                lmd = node
            if depth >= max_depth:
                max_depth = depth
                rmd = node
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        
        if lmd is rmd:
            return lmd
        return self.lca(root, lmd, rmd)
        
    def lca(self, node, lmd, rmd):
        if not node:
            return None
        if node.val==lmd.val or node.val==rmd.val:
            return node
        
        lh = self.lca(node.left, lmd, rmd)
        rh = self.lca(node.right, lmd, rmd)
        
        if lh and rh:
            return node
        if lh and not rh:
            return lh
        if rh and not lh:
            return rh
        return None
        

