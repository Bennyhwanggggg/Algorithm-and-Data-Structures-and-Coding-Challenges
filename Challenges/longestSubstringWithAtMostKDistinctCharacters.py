"""
Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""

"""
Sliding window with dict
Time: O(N) => O(Nk) in case of N distinct characters in the string
Space: O(K)
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not len(s) or len(s) <= k:
            return len(s)
        
        i, j = 0, 0
        res = 0
        seen = dict()
        while j < len(s):
            seen[s[j]] = seen.get(s[j], 0) + 1
            while len(seen) > k:
                seen[s[i]] -= 1
                if seen[s[i]] == 0:
                    del seen[s[i]]  # Average O(1), worse case O(N)
                i += 1
            res = max(res, j-i+1)
            j += 1
        return res
        
