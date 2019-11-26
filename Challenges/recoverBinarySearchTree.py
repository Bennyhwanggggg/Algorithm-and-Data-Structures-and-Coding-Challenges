"""
Recovery Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Inorder or Morris traversal

Keep track of prev and if prev is larger than curr, we know something is wrong (in order traversal of binary search tree should be an ordered list)

Explanation
I don't have any new ideas; just a cool way to implement an old idea.

Use whatever inorder traversal you like (recursion/stack = O(log n) extra space, Morris = O(1) extra space). As most people have figured out pretty easily, the idea is to remember the last value you saw and compare it with the current value. If lastValue > currentValue, then we know that something is "wrong", but it's not immediately clear which values have to be swapped.

There are 2 cases: The values that need to be swapped are either adjacent or not adjacent. If they're adjacent, then there will be one "drop"; if they're not adjacent, then there will be two "drops".

adjacent: ... _ < _ < A > B < _ < _ ...
                      ^^^^^
                      drop #1

not adjacent: ... _ < _ < A > X < _ < Y > B < _ < _ ... (X may be the same as Y, but it's irrelevant)
                          ^^^^^       ^^^^^
                          drop #1     drop #2
In both cases, we want to swap A and B. So the idea is to keep a drops array and append a tuple of (lastNode, currentNode) whenever we come across lastValue > currentValue. At the end of the traversal, the drops array must have either 1 or 2 tuples (otherwise, there would be more than 2 nodes that need to be swapped).

Here's the clear but not-so-clean way to swap them:

if len(drops) == 1: # drops == [(A, B)]
    drops[0][0].val, drops[0][1].val = drops[0][1].val, drops[0][0].val
else: # drops == [(A, X), (Y, B)]
    drops[0][0].val, drops[1][1].val = drops[1][1].val, drops[0][0].val
Here's the clean but not-so-clear way that gets rid of the conditional branching:

drops[0][0].val, drops[-1][1].val = drops[-1][1].val, drops[0][0].val
"""
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr, prev = root, TreeNode(-float('inf'))
        toSwap = []
        stack = []
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            node = stack.pop()
            if node.val < prev.val:
                toSwap.append((prev, node))
            
            prev = node
            curr = node.right
        
        toSwap[0][0].val, toSwap[-1][1].val = toSwap[-1][1].val, toSwap[0][0].val 
        

