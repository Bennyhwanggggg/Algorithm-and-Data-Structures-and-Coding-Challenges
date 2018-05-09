class Solution:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Only at most one character can appear odd number of times.
        charmap = dict()
        for c in s:
            if c not in charmap:
                charmap[c] = 1
            else:
                charmap[c] += 1
        oddcount = 0
        for c in charmap:
            if charmap[c]%2:
                oddcount += 1
            if oddcount >= 2:
                return False
        return True