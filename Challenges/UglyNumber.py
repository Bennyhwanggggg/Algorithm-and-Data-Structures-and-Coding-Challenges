class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        for x in [2, 3, 5]:
            while not num % x:
                num = num / x

        return num == 1
