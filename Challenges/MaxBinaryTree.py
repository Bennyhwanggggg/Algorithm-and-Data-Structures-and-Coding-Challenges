# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            max_ind, max_val = max(enumerate(nums), key=lambda x: x[1])
            node = TreeNode(max_val)
            node.left = self.constructMaximumBinaryTree(nums[:max_ind])
            node.right = self.constructMaximumBinaryTree(nums[max_ind+1:])
            return node