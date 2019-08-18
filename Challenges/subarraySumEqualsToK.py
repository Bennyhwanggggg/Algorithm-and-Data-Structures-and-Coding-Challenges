"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

"""
Sliding Window With accumulative sum

Time: O(N)
Space: O(N)
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = dict()
        counts[0] = 1
        curr_sum = 0
        res = 0
        for n in nums:
            curr_sum += n
            if curr_sum - k in counts:
                res += counts[curr_sum - k]
            counts[curr_sum] = counts.get(curr_sum, 0) + 1
        return res
