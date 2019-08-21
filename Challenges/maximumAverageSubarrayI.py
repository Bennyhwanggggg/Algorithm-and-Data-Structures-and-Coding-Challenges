"""
Maximum Average Subarray I

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 

Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

"""
Sliding Window
Time: O(n)
Space: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left, right = 0, k
        curr_sum = sum(nums[:k])
        res = curr_sum/k
        while right < len(nums):
            curr_sum -= nums[left]
            left += 1
            curr_sum += nums[right]
            right += 1
            res = max(res, curr_sum/k)
        return res

