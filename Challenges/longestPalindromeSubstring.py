"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
Expand Around Center

We observe that a palindrome mirrors around its center. Therefore, a palindrome can be expanded from its center, and there are only 2n−1 such centers.

You might be asking why there are 2n - 1 but not n centers? The reason is the center of a palindrome can be in between two letters. Such palindromes have even number of letters (such as "abba") and its center are between the two 'b's.

Time complexity : O(n^2) Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

Space complexity: O(1). 
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expand(s, i, i)
            len2 = self.expand(s, i, i+1)
            longest = max(len1, len2)
            if longest > end - start:
                start = i - (longest-1)//2
                end = i + longest//2
        return s[start:end+1]
        
    def expand(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j-i-1

