"""
Longest Repeating Substring

Given a string S, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

 

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.
Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.
Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.
 

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500

"""

"""
Binary Search + hashset
Time: O(Nlog(N))
Space: O(N)
"""
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        n = len(S)
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = (left + right) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1
               
        return left - 1
    
    def search(self, length: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - length + 1):
            tmp = S[start:start + length]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1

