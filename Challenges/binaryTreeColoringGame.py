"""
Binary Tree Coloring Game

Two players play a turn based game on a binary tree.  We are given the root of this binary tree, and the number of nodes n in the tree.  n is odd, and each node has a distinct value from 1 to n.

Initially, the first player names a value x with 1 <= x <= n, and the second player names a value y with 1 <= y <= n and y != x.  The first player colors the node with value x red, and the second player colors the node with value y blue.

Then, the players take turns starting with the first player.  In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an uncolored neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)

If (and only if) a player cannot choose such a node in this way, they must pass their turn.  If both players pass their turn, the game ends, and the winner is the player that colored more nodes.

You are the second player.  If it is possible to choose such a y to ensure you win the game, return true.  If it is not possible, return false.

 

Example 1:


Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
Output: true
Explanation: The second player can choose the node with value 2.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Intuition
The first player colors a node,
there are at most 3 nodes connected to this node.
Its left, its right and its parent.
Take this 3 nodes as the root of 3 subtrees.

The second player just color any one root,
and the whole subtree will be his.
And this is also all he can take,
since he cannot cross the node of the first player.


Explanation
count will recursively count the number of nodes,
in the left and in the right.
n - left - right will be the number of nodes in the "subtree" of parent.
Now we just need to compare max(left, right, parent) and n / 2


Complexity
Time O(N)
Space O(height) for recursion
"""

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) / 2 < max(max(c), n - sum(c) - 1)

