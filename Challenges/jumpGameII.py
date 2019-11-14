"""
Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
"""

"""
Greedy, always, take the furtherest one, between current edge and current point

The idea is to maintain two pointers left and right, where left initialy set to be 0 and right set to be nums[0].
So points between 0 and nums[0] are the ones you can reach by using just 1 jump.
Next, we want to find points I can reach using 2 jumps, so our new left will be set equal to right, and our new right will be set equal to the farest point we can reach by two jumps. which is:
right = max(i + nums[i] for i in range(left, right + 1)

Time, Space: O(N)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: 
            return 0
        
        l, r = 0, nums[0]
        times = 1
        
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
            
        return times

