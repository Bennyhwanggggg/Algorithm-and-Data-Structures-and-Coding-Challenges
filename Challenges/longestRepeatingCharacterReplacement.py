"""
Longest Repeating Character Replacement

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.
 

Example 2:

Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
"""

"""
Sliding window

Keep track of all character seen and their count, when we have made more than k changes in the window, slide right

The problem says that we can make at most k changes to the string (any character can be replaced with any other character). So, let's say there were no constraints like the k. Given a string convert it to a string with all same characters with minimal changes. The answer to this is

length of the entire string - number of times of the maximum occurring character in the string

Given this, we can apply the at most k changes constraint and maintain a sliding window such that

(length of substring - number of times of the maximum occurring character in the substring) <= k

Time: O(NK)
Space: O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = [0]*26
        res = ''
        left = 0
        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            seen[idx] += 1
            if right-left+1-max(seen) > k:
                key = ord(s[left]) - ord('A')
                seen[key] -= 1
                left += 1
            if right-left+1 > len(res):
                res = s[left:right+1]
        return len(res)

