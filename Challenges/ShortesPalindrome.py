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
