"""
Sorted Array To BST

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""

class Solution_iterative:
    def sortedArrayToBST(self, nums):
        if not nums:
            return []

        from collections import deque
        root = TreeNode(None)
        queue = deque([root])
        leftbound = deque([0])
        rightbound = deque([len(nums) - 1])
        while queue:
            node = queue.popleft()
            left = leftbound.popleft()
            right = rightbound.popleft()
            mid = (left + right) // 2
            node.val = nums[mid]

            if left <= mid - 1:
                node.left = TreeNode(None)
                queue.append(node.left)
                leftbound.append(left)
                rightbound.append(mid - 1)

            if right >= mid + 1:
                node.right = TreeNode(None)
                queue.append(node.right)
                leftbound.append(mid + 1)
                rightbound.append(right)

        return root


class Solution_recursive_leftboundary_rightboundary:
    def sortedArrayToBST(self, nums):
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, l, r):
        if l > r:
            return None
        mid = (l + r) // 2
        root = TreeNode(nums[mid])
        root.left = self.helper(nums, l, mid - 1)
        root.right = self.helper(nums, mid + 1, r)
        return root


class Solution_recursive_slicing_array:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root
