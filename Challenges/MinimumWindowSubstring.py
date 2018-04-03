class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t):
            return ''

        need = {}
        missing = len(t)
        for char in t:
            if char not in need:
                need[char] = 1
            else:
                need[char] += 1

        i = I = J = 0
        for j, c in enumerate(s, 1):
            if c in need:
                if need[c] > 0:
                    missing -= 1
                need[c] -= 1
            while i < j and not missing:
                if not J or j - i < J - I:
                    I, J = i, j
                if s[i] not in need:
                    i += 1
                    continue
                else:
                    need[s[i]] += 1
                    if need[s[i]] > 0:
                        missing += 1
                    i += 1
        return s[I:J]

