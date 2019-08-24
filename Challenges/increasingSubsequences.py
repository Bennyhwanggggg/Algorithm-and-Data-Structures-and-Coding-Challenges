"""
Increasing Subsequences

Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

 

Example:

Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
 

Note:

The length of the given array will not exceed 15.
The range of integer in the given array is [-100,100].
The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
"""

"""
Backtracking

Time: O(n!)
Space: O(n!)
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def backtrack(arr, curr):
            if len(curr) >= 2:
                res.add(tuple(curr))
            
            for idx, n in enumerate(arr):
                if len(curr) == 0:
                    backtrack(arr[idx+1:], [n])
                elif len(curr) != 0 and n >= curr[-1]:
                    backtrack(arr[idx+1:], curr + [n])
        
        backtrack(nums, [])
        return [list(sol) for sol in res]

"""
DP?
"""
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = []
        Set = set()
        for i in range(len(nums)):
            stack.append([])
            for j in range(i-1, -1, -1):
                if nums[j] <= nums[i]:
                    stack[i].append([nums[j], nums[i]])
                    Set.add((nums[j], nums[i]))
                    for sequence in stack[j]:
                        stack[i].append(sequence + [nums[i]])
                        Set.add(tuple(stack[i][-1]))
                if nums[j] == nums[i]:
                    break
        return list(Set)
