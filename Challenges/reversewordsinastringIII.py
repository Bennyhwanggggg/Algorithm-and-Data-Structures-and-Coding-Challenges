class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        return ' '.join(words)