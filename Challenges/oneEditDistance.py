"""
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
"""

"""
Intuition
If there is no differences between the first len(s) characters, only two situations are possible :

The strings are equal.

The strings are one edit away distance.
Now what if there is a different character so that s[i] != t[i].

If the strings are of the same length, all next characters should be equal to keep one edit away distance. To verify it, one has to compare the substrings of s and t both starting from the i + 1th character.

If t is one character longer than s, the additional character t[i] should be the only difference between both strings. To verify it, one has to compare a substring of s starting from the ith character and a substring of t starting from the i + 1th character.



One Pass
Time: O(N) in the worst case when string lengths are close enough abs(ns - nt) <= 1, where N is a number of characters in the longest string. \mathcal{O}(1)O(1) in the best case when abs(ns - nt) > 1.
Space: O(N) from producing substrings since strings are immutable in Python
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            s, t = t, s
        if len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                # if the strings have the same length, we must 
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                else:
                    # if different length, can only delete to get same
                    return s[i:] == t[i+1:]
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character. 
        return ns+1 == nt


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False

        posS = 0
        posT = 0
        m = len(s)
        n = len(t)

        if abs(m - n) > 1:
            return False

        count = 0
        while posS < m and posT < n:
            if s[posS] != t[posT]:
                count += 1
                if count > 1:
                    return False
                if m == n:
                    posS += 1
                    posT += 1
                elif m > n:
                    posS += 1
                elif m < n:
                    posT += 1
            else:
                posS += 1
                posT += 1
        return True
