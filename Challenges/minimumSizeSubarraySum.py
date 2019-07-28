"""
Minimum Size Subarray Sum

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

"""
Two pointer
Time: O(N)
Space: O(1)
"""
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        left, right, curr = 0, 0, 0
        minLen = len(nums) + 1
        while right < len(nums):
            curr += nums[right]
            while curr >= s:
                minLen = min(minLen, right - left + 1)
                curr -= nums[left]
                left += 1
            right += 1

        return minLen if minLen != (len(nums) + 1) else 0


