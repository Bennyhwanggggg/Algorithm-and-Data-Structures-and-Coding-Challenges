class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        minlen = 0
        if not s:
            return minlen
        chars = {}
        j = 0
        for i in range(len(s)):
            if s[i] in chars:
                j = max(j, chars[s[i]] + 1)
            chars[s[i]] = i
            minlen = max(minlen, i - j + 1)

        return minlen
