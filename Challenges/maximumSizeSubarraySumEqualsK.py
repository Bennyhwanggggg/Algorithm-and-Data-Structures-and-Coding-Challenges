"""
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Note:
The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Example 1:

Input: nums = [1, -1, 5, -2, 3], k = 3
Output: 4 
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.
Example 2:

Input: nums = [-2, -1, 2, 1], k = 1
Output: 2 
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
Follow Up:
Can you do it in O(n) time?
"""

"""
Sliding Window with acuumulative sum

Time: O(N)
Space: O(N)
"""
class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_table = {}  # key: sum(nums[:i+1]), value: i
        total = 0
        max_len = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sum_table.keys():
                sum_table[total] = i
            remain = total - k
            if remain == 0:
                max_len = max(i + 1, max_len)
            elif remain in sum_table.keys():
                max_len = max(i - sum_table[remain], max_len)

        return max_len
