"""
Shortest Palindrome if you can add characters

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
"""

"""
Lets take a string "abcbabcaba". Let us consider 2 pointers ii and jj. Initialize i = 0i=0. Iterate over jj from n-1n−1 to 00, incrementing ii each time s[i]==s[j]. Now, we just need to search in range [0,i). This way, we have reduced the size of string to search for the largest palindrome substring from the beginning. The range [0,i) must always contain the largest palindrome substring. The proof of correction is that: Say the string was a perfect palindrome, ii would be incremented nn times. Had there been other characters at the end, ii would still be incremented by the size of the palindrome. Hence, even though there is a chance that the range [0,i) is not always tight, it is ensured that it will always contain the longest palindrome from the beginning.

The best case for the algorithm is when the entire string is palindrome and the worst case is string like aababababababa", wherein ii first becomes 1212(check by doing on paper), and we need to recheck in [0,12) corresponding to string "aabababababa". Again continuing in the same way, we get i=10. In such a case, the string is reduced only by as few as 2 elements at each step. Hence, the number of steps in such cases is linear (n/2).

This reduction of length could be easily done with the help of a recursive routine, as shown in the algorithm section.

Algorithm

The routine \text{shortestPalindrome}shortestPalindrome is recursive and takes string ss as parameter:

Initialize i=0i=0
Iterate over jj from n-1n−1 to 00:
If s[i]==s[j], increase ii by 11
If ii equals the size of ss, the entire string is palindrome, and hence return the entire string ss.
Else:
Return reverse of remaining substring after ii to the end of string + \text{shortestPalindrome}shortestPalindrome routine on substring from start to index i-1i−1 + remaining substring after ii to the end of string.

Time: O(n^2) Each iteration of shortestPalindrome is linear in size of substring and the maximum number of recursive calls can be n/2 times as shown in the Intuition section.
Space: O(n) extra space for remaining string
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        for j in range(n-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        
        if i == n:
            return s
        
        remain = s[i:n]
        reverse_remain = remain[::-1]
        return reverse_remain + self.shortestPalindrome(s[0:i]) + s[i:]
        


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def LPS(p):
            lps = [0] * len(p)
            l = 0
            for i in range(1, len(p)):
                while l > 0 and p[i] != p[l]:
                    l = lps[l - 1]
                if p[i] == p[l]:
                    l += 1
                    lps[i] = l
            return lps

        lps = LPS(s)
        i = 0;
        j = len(s) - 1
        while i < j:
            while i > 0 and s[i] != s[j]:
                i = lps[i - 1]
            if s[i] == s[j]:
                i += 1
            j -= 1
        return s[(i + j) + 1:len(s)][::-1] + s

        # may not work if input string contain special values
        # return s[lps[len(lps)-1]:len(s)][::-1] + s
