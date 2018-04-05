class Solution:
    def reverseWords(self, string):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        self.reverse(string, 0, len(string))
        i = 0
        for j in range(len(string) + 1):
            if j == len(string) or string[j] == " ":
                self.reverse(string, i, j)
                i = j + 1

    def reverse(self, s, l, r):
        for i in range((r - l) // 2):
            temp = s[l + i]
            s[l + i] = s[r - 1 - i]
            s[r - 1 - i] = temp