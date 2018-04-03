class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == t:
            return False

        posS = 0
        posT = 0
        m = len(s)
        n = len(t)

        if abs(m - n) > 1:
            return False

        count = 0
        while posS < m and posT < n:
            if s[posS] != t[posT]:
                count += 1
                if count > 1:
                    return False
                if m == n:
                    posS += 1
                    posT += 1
                elif m > n:
                    posS += 1
                elif m < n:
                    posT += 1
            else:
                posS += 1
                posT += 1
        return True