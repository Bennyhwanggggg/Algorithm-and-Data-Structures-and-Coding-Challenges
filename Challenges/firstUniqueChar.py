class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        seen = {}
        for c in s:
            if c not in seen:
                seen[c] = 0
            seen[c] += 1

        for pos, c in enumerate(s):
            if seen[c] == 1:
                return pos
        return -1
