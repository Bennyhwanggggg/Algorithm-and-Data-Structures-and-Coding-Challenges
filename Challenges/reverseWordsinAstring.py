class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        w = s.split()
        return ' '.join(w[::-1])