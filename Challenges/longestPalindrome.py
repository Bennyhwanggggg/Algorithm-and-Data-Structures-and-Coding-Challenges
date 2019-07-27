"""
Longest Palindrome

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = collections.Counter(s)
        
        res = 0
        odd_exist = False
        for val in seen.values():
            if val%2 == 0:
                res += val
            else:
                odd_exist = True
                res += val-1
        return res if not odd_exist else res+1

