"""
Max Consecutive Ones

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for n in nums:
            if n == 1:
                curr += 1
                res = max(curr, res)
            else:
                curr = 0
        return res

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = 0
        count = 0
        for i in nums:
            if i:
                count += 1
                if count > MAX:
                    MAX = count
            else:
                count = 0

        return MAX
