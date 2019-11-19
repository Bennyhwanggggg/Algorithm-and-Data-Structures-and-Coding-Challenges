"""
Largest BST Subtree

Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.

Example:

Input: [10,5,15,1,8,null,7]

   10 
   / \ 
  5  15 
 / \   \ 
1   8   7

Output: 3
Explanation: The Largest BST Subtree in this case is the highlighted one.
             The return value is the subtree's size, which is 3.
Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Brute force
Time: O(N^2)
"""
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def isBST(node):
            if not node:
                return 0
            return isBSTHelper(node, -float('inf'), float('inf'))
            
            
        def isBSTHelper(node, left, right):
            if not node:
                return 0
            if node.val <= left or node.val >= right:
                return -1
            leftNodes = isBSTHelper(node.left, left, node.val)
            rightNodes = isBSTHelper(node.right, node.val, right)
            if leftNodes < 0 or rightNodes < 0:
                return -1
            return leftNodes+rightNodes+1
        
        def dfs(node):
            if not node:
                return
            self.res = max(self.res, isBST(node))
            dfs(node.left)
            dfs(node.right)
        
        self.res = 0
        dfs(root)
        return self.res
        
        
"""
Algorithm: in order to solve in O(n) you need to do a bottoms-up. At every node you need to pass back 4 items to meet all constraints starting from the leaves:

whether the subtree is a valid BST or not (bool)
how many nodes
min value in this subtree
max value in this subtree
Armed with this information you can begin checking for conditions which would make the current node no longer a valid BST. The first case -- confirm left exists, if it does, ensure that the node is greater than the max for that subtree. Next, confirm that if the right tree exists and that the minimum value there is greater than the current node. If both these hold, then the current node can form a valid BST with the left and right subtrees, thus update the result with the total number of nodes which form the new tree. For invalid cases ensure to return a False for the valid variable, the rest of the variables won't matter.
"""
class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def dfs(node):
            if not node:
                return True, 0, float('inf'), -float('inf')
            leftIsBST, leftCount, leftMin, leftMax = dfs(node.left)
            rightIsBST, rightCount, rightMin, rightMax = dfs(node.right)
            if not leftIsBST or not rightIsBST:
                return False, 0, float('inf'), -float('inf')
            if leftMax < node.val < rightMin:
                self.res = max(self.res, leftCount+rightCount+1)
                return True, leftCount+rightCount+1, min(node.val, leftMin, rightMin), max(node.val, leftMax, rightMax)
            return False, 0, float('inf'), -float('inf')
            
        if not root:
            return 0
        self.res = -float('inf')
        dfs(root)
        return self.res        


"""
Same as first one, from top to bottom and terminate at first bst found

Apprently fastest runtime
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        
        def isBST(root):
            if not root:
                return 0
            return isBSTHelper(root, -float('inf'), float('inf'))
        
        def isBSTHelper(node, left, right):
            if not node:
                return 0
            if left >= node.val or right <= node.val:
                return -1
            left = isBSTHelper(node.left, left, node.val)
            right = isBSTHelper(node.right, node.val, right)
            if left < 0 or right < 0:
                return -1
            return left + right + 1
        self.res = 0
        if not root:
            return 0
        count = isBST(root)
        if count >= 0:
            return count
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))
            
