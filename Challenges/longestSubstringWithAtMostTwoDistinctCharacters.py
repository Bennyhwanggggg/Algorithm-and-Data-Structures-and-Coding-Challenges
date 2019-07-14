"""
Longest Substring with At Most Two Distinct Characters

Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:

Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:

Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""

"""
Sliding Window
Time: O(N)
Space: O(1) since only use hashmap with at most 3 element
"""
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not len(s):
            return 0
        i, res = 0, 0
        count = dict()
        for j, x in enumerate(list(s)):
            count[x] = count.get(x, 0) + 1
            while len(count) > 2:
                count[s[i]] -= 1
                if count[s[i]] == 0:
                    del count[s[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
