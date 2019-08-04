"""
Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

"""
Greedy
Time: O(N)
Space: O(1)
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach >= i and i + nums[i] > reach:
                reach = i + nums[i]
        return reach >= len(nums)-1

"""
DP

dp[i] as the maximum index one can jump after reach index i

Time: O(N)
Space: O(1)
"""
class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<2:
            return True
        dp    = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1]<i:
                return False
            dp[i] = max(dp[i-1], i + nums[i])
        return dp[-1]>=len(nums)-1

