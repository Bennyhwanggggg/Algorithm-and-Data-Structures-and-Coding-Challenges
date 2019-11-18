"""
House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""

"""
Notice that the first house and the last house can not be both robbed, so we have rob(nums) = max(rob(nums[1:], nums[:-1]). Since there are no circles in both nums[1:] and nums[:-1], we can simply apply the answers from House Rob


DP
Time: O(N)
Space: O(N)
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(nums):
            dp = [0]*len(nums)
            dp[0] = nums[0]
            if len(nums) == 1:
                return nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], nums[i]+dp[i-2])
            
            return dp[-1]
        
        if not len(nums):
            return 0
        elif len(nums) == 1:
            return nums[0]
        return max(rob(nums[1:]), rob(nums[:-1]))

"""
Time: O(N)
Space: O(1)
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def simple_rob(nums):
            rob, not_rob = 0, 0
            for num in nums:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)
        
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(simple_rob(nums[1:]), simple_rob(nums[:-1]))
