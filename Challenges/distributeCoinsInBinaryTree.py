"""
Distributed Coins In Binary Tree

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

 

Example 1:



Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
Example 2:



Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
Example 3:



Input: [1,0,2]
Output: 2
Example 4:



Input: [1,0,0,null,3]
Output: 4
 

Note:

1<= N <= 100
0 <= node.val <= N
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
DFS

For each subtree or each DFS recursion, I return two values: (1) current root balance and (2) number of moves required to make subtree balanced.

First let me explain the terms here.
Suppose I have a subtree as:

  0
 / \
1   0
The root balance would be -2, indicating this subtree needs two coins in. And number of moves would be 3, indicating 3 moves are needed to make entire subtree balanced
(1 moves to give root node a coin from parent node, 2 moves to give right node a coin from parent node).
Here is another example:

  3
 / \
1   0
The root balance would be 1, indicating this subtree needs one coin out. And number of moves would be 2, indicating 2 moves are needed to make entire subtree balanced
(1 move to give right node a coin from root node, 1 move to give parent node a coin from root node to balance root node).

And here is an assumption to simplify the problem here.
Since we just need to count to number of moves, the sequence of coin moving doesn't matter, which simplify the issue. So, we can assume some node's coin balance could be negative. And to keep a subtree balanced, we can acquire(or sending) as many coin as neccessary from parent node to balance subtree first, even this would make parent node negative.
Therefore, DFS can be implemented here to balance each subtree and aggregate the number of moves.

And how to calculate current subtree's balance and number of moves?

Down to the leaf node, the balance would be node.val-1 (one coin is needed for node itself). Then we need to either send abs(balance) coins from parent node to it, or send abs(balance) coins from it to parent node. And each coin sending cost 1 moves so total number of moves is abs(balance).

Then for a subtree, we have child node's balance (remember each subtree eventually either sends coins to or requires coins from parent node), and number of moves that subtree used to keep itself balanced, from DFS call. And subtree's balance is left node's balance + right node's balance + root node's balance = lbal+rbal+node.val-1.
As for number of move, since we have already counted children trees' moves, we just need to count number of moves to make root node balanced. Similiar as leaf node, the number of moves is abs(balance) and total number of moves is left tree's moves + right tree's moves + abs(balance) = lcnt+rcnt+abs(balance).

And here is an example for a complete case:
If a tree is [1, left, right], left = [3,1,0], right = [0,1,1]. The left balance is 1, means after left balanced itself it, moves one coin to root. So left becomes [1,1,1] and parent tree becomes [2, left, right]. The right balance is -1, means after right balanced itself, it takes one coin from root. So right becomes [1,1,1] and parent tree becomes [1, left, right] and balanced. Left's count is 2, indicating it takes two steps to balance itself while right's count is 1, indicating it takes one step to balance itself. The parent tree is balanced since left balance + right balance = 0 which also means parent tree doesn't need to move out or take in any coins. And total number of steps is left's count + right's count + abs(balance) = 3.

Time: O(N)
Space: O(N)
"""
class Solution:
    def distributeCoins(self, root: TreeNode, pre=None) -> int:
        if not root: 
            return 0
        res = self.distributeCoins(root.left, root) + self.distributeCoins(root.right, root)
        if pre: 
            pre.val += root.val - 1
        return res + abs(root.val - 1)
    
class Solution:
    def distributeCoins(root):
        def dfs(node):
            if not node: return 0, 0
            (lbal, lcnt), (rbal, rcnt) = dfs(node.left), dfs(node.right)
            bal = node.val + lbal + rbal -1
            return bal, lcnt + rcnt + abs(bal)
        return dfs(root)[1]

