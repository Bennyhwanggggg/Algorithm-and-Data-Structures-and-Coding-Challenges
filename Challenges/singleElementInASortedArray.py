"""
Single Element In A Sorted Array

Given a sorted array consisting of only integers where every element appears exactly twice except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
"""

"""
Bit manipulation
Time: O(N)
Space: O(1)
"""
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        seen = 0
        for n in nums:
            seen ^= n
        return seen
    
"""
Binary Search
Time: O(log(n))
Space: O(1)
"""
class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return None
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l)/2
            if m - 1 < l or m + 1 > r:
                break
            if m % 2 == 0:
                if nums[m] == nums[m+1]:
                    l = m + 2
                else:
                    r = m
            else:
                if nums[m] == nums[m-1]:
                    l = m + 1
                else:
                    r = m
        return nums[l]

