"""
Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

"""
Sliding Window
Slide a window accross while keeping counts of the current characters in window
only try to contract when we have a working window
Time, space: O(S+T)
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        
        counts = collections.Counter(t)
        required = len(counts)
        
        l, r = 0, 0
        currUnique = 0
        windowCounts = dict()
        
        res = (float('inf'), l, r)
        
        while r < len(s):
            c = s[r]
            windowCounts[c] = windowCounts.get(c, 0) + 1
            
            if c in counts and windowCounts[c] == counts[c]:
                currUnique += 1
            
            while l <= r and currUnique == required:
                c = s[l]
                if r - l + 1 < res[0]:
                    res = (r-l+1, l, r)
                
                windowCounts[c] -= 1
                if c in counts and windowCounts[c] < counts[c]:
                    currUnique -= 1
                
                l += 1
            
            r += 1
        return '' if res[0] == float('inf') else s[res[1]:res[2]+1]
        
        
        
            

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t):
            return ''

        need = {}
        missing = len(t)
        for char in t:
            if char not in need:
                need[char] = 1
            else:
                need[char] += 1

        i = I = J = 0
        for j, c in enumerate(s, 1):
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            while i < j and not missing:
                if not J or j - i < J - I:
                    I, J = i, j
                if s[i] not in need:
                    i += 1
                    continue
                else:
                    need[s[i]] += 1
                    if need[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

