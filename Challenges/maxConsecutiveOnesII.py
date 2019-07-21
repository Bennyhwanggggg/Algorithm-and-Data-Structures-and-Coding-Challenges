"""
Max Consecutive Ones II

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Example 1:
Input: [1,0,1,1,0]
Output: 4
Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
    After flipping, the maximum number of consecutive 1s is 4.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
Follow up:
What if the input numbers come in one by one as an infinite stream? In other words, you can't store all numbers coming from the stream as it's too large to hold in memory. Could you solve it efficiently?
"""

"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        K = 1
        for j in range(len(nums)):
            K -= 1 - nums[j]
            if K < 0:
                K += 1 - nums[i]
                i += 1
        return j - i + 1

"""
store the length of previous and current consecutive 1's (separated by the last 0) as pre and curr , respectively. 

Whenever we get a new number, update these two variables accordingly. The consecutive length would be pre + 1 + curr, where the 1 is a zero that got flipped to 1. (note that pre is initialized to -1, meaning that we haven't seen any 0 yet)
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, curr, maxlen = -1, 0, 0
        for i in nums:
            if i == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            maxlen = max(maxlen, pre + curr + 1)

        return maxlen
