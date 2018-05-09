class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        if not s:
            return 0

        num = 0
        i = len(s) - 1
        while i >= 0:
            num += symbols[s[i]]
            if i > 0 and symbols[s[i]] > symbols[s[i - 1]]:
                num -= symbols[s[i - 1]]
                i -= 1
            i -= 1
        return num