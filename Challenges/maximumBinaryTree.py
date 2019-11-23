"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
Note: The size of the given array will be in the range [1,1000].
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Approach 1: Recursive Solution
The current solution is very simple. We make use of a function construct(nums, l, r), which returns the maximum binary tree consisting of numbers within the indices ll and rr in the given numsnums array(excluding the r^{th}r 
th
  element).

The algorithm consists of the following steps:

Start with the function call construct(nums, 0, n). Here, nn refers to the number of elements in the given numsnums array.

Find the index, max_i, of the largest element in the current range of indices (l:r−1). Make this largest element, nums[max_i] as the local root node.

Determine the left child using construct(nums, l, max_i). Doing this recursively finds the largest element in the subarray left to the current largest element.

Similarly, determine the right child using construct(nums, max_i + 1, r).

Return the root node to the calling function.
"""
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        res = self.construct(nums)
        return res

    def construct(self, nums):
        maxNum = max(nums)
        maxIdx = nums.index(maxNum)
        root = TreeNode(maxNum)
        if len(nums[:maxIdx]):
            root.left = self.construct(nums[:maxIdx])
        if len(nums[maxIdx+1:]):
            root.right = self.construct(nums[maxIdx+1:])
        return root
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        maxNum = max(nums)
        maxIdx = nums.index(maxNum)
        
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[:maxIdx])
        root.right = self.constructMaximumBinaryTree(nums[maxIdx+1:])
        return root

