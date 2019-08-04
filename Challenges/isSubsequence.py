"""
Is Subsequence

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""

"""
Brute Force
Time: O(T)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                if i == len(s):
                    return True
            else:
                j += 1
        return False

"""
Binary Search using indices, better when there are many incoming data
Time: O(T + Slog(T))
"""
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = collections.defaultdict(list)
        for i in xrange(0, len(t)):
            d[t[i]].append(i)
        start = 0
        for c in s:
            idx = bisect.bisect_left(d[c], start)
            if len(d[c]) == 0 or idx >= len(d[c]):
                return False
            start = d[c][idx] + 1
        return True

