"""
Move Zeros

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

"""
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero = 0
        for i in range(len(nums)):
          if nums[i]:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        for n in nums:
            if n != 0:
                count += 1

        count2 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count2] = nums[i]
                count2 += 1

        for i in range(count, len(nums)):
            nums[i] = 0
