"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

"""
Two scan binary search to find each end
Time: O(log n)
spcae: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        
        if nums[low] != target:
            return [-1, -1]

        res = [low]
        high = len(nums) - 1
        
        while low < high:
            mid = ((low + high) // 2) + 1
            if nums[mid] >
            target:
                high = mid-1
            else:
                low = mid
        res.append(high)
        return res
        
                

