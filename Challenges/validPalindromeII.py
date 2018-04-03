class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                temp1 = s[:left] + s[left + 1:]
                temp2 = s[:right] + s[right + 1:]
                if temp1 == temp1[::-1] or temp2 == temp2[::-1]:
                    return True
                else:
                    return False

            left += 1
            right -= 1
        return True
