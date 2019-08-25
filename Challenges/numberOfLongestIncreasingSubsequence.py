"""
Number of Longest Increasing Subsequence

Given an unsorted array of integers, find the number of longest increasing subsequence.

Example 1:
Input: [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:
Input: [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
"""

"""
In the Longest Increasing Subsequence problem, the DP array simply had to store the longest length. In this variant, each element in the DP array needs to store two things: (1) Length of longest subsequence ending at this index and (2) Number of longest subsequences that end at this index. I use a two element list for this purpose.

In each loop as we build up the DP array, find the longest length for this index and then sum up the numbers at these indices that contribute to this longest length.

Here I provide two versions: (1) A slower but easier to understand version and (2) Much faster and optimized version
"""
class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Time: O(n^2)
        # Space: O(n)
        dp, longest = [[1, 1] for i in range(len(nums))], 1
        for i, num in enumerate(nums):
            curr_longest, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    curr_longest = max(curr_longest, dp[j][0] + 1)
            for j in range(i):
                if dp[j][0] == curr_longest - 1 and nums[j] < num:
                    count += dp[j][1]
            dp[i] = [curr_longest, max(count, dp[i][1])]
            longest = max(curr_longest, longest)
        return sum([item[1] for item in dp if item[0] == longest])


# The counting step can be optimized such that we don't count from the start when we find a longer max_len. This improved the speed from 10% to 88%.

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[1, 1] for i in range(len(nums))]
        max_for_all = 1
        for i, num in enumerate(nums):
            max_len, count = 1, 0
            for j in range(i):
                if nums[j] < num:
                    if dp[j][0] + 1 > max_len:
                        max_len = dp[j][0] + 1
                        count = 0 
                    if dp[j][0] == max_len - 1:
                        count += dp[j][1]
            dp[i] = [max_len, max(count, dp[i][1])]
            max_for_all = max(max_len, max_for_all)
        return sum([item[1] for item in dp if item[0] == max_for_all])
