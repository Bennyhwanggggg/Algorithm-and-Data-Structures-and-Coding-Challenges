"""
Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

"""
Time, Space: O(N)
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSet = set(nums)
        for n in range(len(nums)+1):
            if n not in numsSet:
                return n
            
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

