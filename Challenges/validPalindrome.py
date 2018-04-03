class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s or len(s) == 1:
            return True

        s = "".join(c.lower() for c in s if c.isalnum())
        end = len(s) - 1
        start = 0
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True