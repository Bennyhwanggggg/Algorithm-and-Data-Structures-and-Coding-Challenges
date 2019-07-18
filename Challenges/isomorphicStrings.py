"""
Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
"""

"""
Linear scan
Time: O(n)
Space: O(n)
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        seen = dict()
        for i in range(len(s)):
            if s[i] not in seen.keys() and t[i] not in seen.values():
                seen[s[i]] = t[i]
            else:
                if s[i] not in seen.keys() or seen[s[i]] != t[i]:
                    return False
        return True
    
def isIsomorphic(self, s, t):
    d1, d2 = dict(), dict()
    for v, w in zip(s,t):
        if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
        d1[v], d2[w] = w, v
    return True

