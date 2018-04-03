class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s: return s

        n = len(s)
        result = ""
        dp = [[False] * n for _ in range(n)]
        max_len = 0

        for i in range(n):
            dp[i][i] = True
            max_len = 1
            result = s[i]

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                result = s[i:i + 2]
                max_len = 2

        for j in range(n):
            for i in range(j - 1):
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        result = s[i:j + 1]
                        max_len = j - i + 1

        return result