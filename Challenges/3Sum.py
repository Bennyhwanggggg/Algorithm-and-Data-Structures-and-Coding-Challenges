"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

"""
Use 3 pointers. With each first pointer, do an O(N) scan on remaining
Time: O(n*n)
Space: O(n)
"""
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = set()
        nums.sort() # sort to avoid duplicates, unless order in result doesn't matter
        for i, val in enumerate(nums[:-2]):
            # get rid of duplicates
	    if i >= 1 and val == nums[i-1]:
                continue
            d = set()
            for x in nums[i+1:]:
                n = -val-x
                if x not in d:
                    d.add(n)
                else:
                    res.add((val, n, x))
        return [list(sol) for sol in res]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = set()
        nums.sort()
        for ind, val in enumerate(nums[:-2]):
            seen = set()
            for x in nums[ind+1:]:
                n = -val-x
                if x not in seen:
                    seen.add(n)
                else:
                    result.add((val, x, n))
        return [list(sol) for sol in result]
