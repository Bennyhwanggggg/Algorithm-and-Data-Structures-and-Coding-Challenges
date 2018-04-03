class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if not s or not k:
            return 0

        start = 0
        end = 0
        longest = 0
        chars = {}

        for index in range(len(s)):

            chars[s[index]] = chars.get(s[index], 0) + 1
            while len(chars) > k:
                chars[s[start]] -= 1
                if chars[s[start]] == 0:
                    del chars[s[start]]
                start += 1

            longest = max(longest, index + 1 - start)

        return longest