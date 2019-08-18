"""
Verify Perorder Sequence In Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?
"""

"""
Using Binary Tree's property and stack

We keep updating the lower bound

Time: O(N)
Space: O(N)
"""
class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        lower = -float('inf')
        for x in preorder:
            if x < lower:
                return False
            while stack and x > stack[-1]:
                lower = stack.pop()
            stack.append(x)
        return True
    
"""
Time: O(N)
Space: O(1)

Preorder array can be reused as the stack thus achieve O(1) extra space, since the scanned items of preorder array is always more than or equal to the length of the stack.

At any point, we need to figure out the lower bound for all the values yet to be seen or processed. Now how would be manage that? Visualize a BST.
Initially that lower bound is -INF.
You start pushing all the left most values into a stack. When you find preorder[i] > preorder[i-1], it indicates a right child. We now want to find the predecessor of this right child. The predecessor will serve as new lower bound.
How do we find predecessor? Keep popping till you preorder[i] > st[-1].
"""
class Solution(object):
    def verifyPreorder(self, preorder):
        # stack = preorder[:i], reuse preorder as stack
        lower = -1 << 31
        i = 0
        for x in preorder:
            if x < lower:
                return False
            while i > 0 and x > preorder[i - 1]:
                lower = preorder[i - 1]
                i -= 1
            preorder[i] = x
            i += 1
        return True

