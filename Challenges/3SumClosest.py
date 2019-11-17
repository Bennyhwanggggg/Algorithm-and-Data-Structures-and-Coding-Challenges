"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


"""
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            # do two pointer search
            left, right = i+1, len(nums)-1
            while left < right:
                sumOfThree = nums[i] + nums[left] + nums[right]
                if abs(sumOfThree - target) < abs(res - target):
                    res = sumOfThree
                if sumOfThree > target:
                    right -= 1
                elif sumOfThree < target:
                    left += 1
                else:
                    return sumOfThree
        return res
            
