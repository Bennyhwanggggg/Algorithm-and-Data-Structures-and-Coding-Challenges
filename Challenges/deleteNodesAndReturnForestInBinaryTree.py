"""
Delete Nodes And Return Forest

Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Question analysis
The question is composed of two requirements:

To remove a node, the child need to notify its parent about the child's existance.
To determine whether a node is a root node in the final forest, we need to know [1] whether the node is removed (which is trivial), and [2] whether its parent is removed (which requires the parent to notify the child)
It is very obvious that a tree problem is likely to be solved by recursion. The two components above are actually examining interviewees' understanding to the two key points of recursion:

passing info downwards -- by arguments
passing info upwards -- by return value

If a node is root (has no parent) and isn't deleted,
when will we add it to the result.

Complexity
Time O(N)
Space O(N)
"""
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ans = []
        
        def walk(node, parent_exist):
            if node is None:
                return None
            if node.val in to_delete:
                node.left = walk(node.left, parent_exist=False)
                node.right = walk(node.right, parent_exist=False)
                return None
            else:
                if not parent_exist:
                    ans.append(node)
                node.left = walk(node.left, parent_exist=True)
                node.right = walk(node.right, parent_exist=True)
                return node
        
        walk(root, parent_exist=False)
        return ans
        
        

