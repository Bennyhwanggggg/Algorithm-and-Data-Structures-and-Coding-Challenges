
"""
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = -float('inf')
        if not s:
            return 0
        seen = dict() # keep track of where each character occur last and use those points as starting point
        j = 0
        for i in range(len(s)):
            if s[i] in seen:
                j = max(j, seen[s[i]] + 1) # add one because we cant use that index anymore
            seen[s[i]] = i
            res = max(res, i-j+1)
        return res

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        minlen = 0
        if not s:
            return minlen
        chars = {}
        j = 0
        for i in range(len(s)):
            if s[i] in chars:
                j = max(j, chars[s[i]] + 1)
            chars[s[i]] = i
            minlen = max(minlen, i - j + 1)

        return minlen
