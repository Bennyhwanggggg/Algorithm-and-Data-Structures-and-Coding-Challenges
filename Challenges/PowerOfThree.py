class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        while not n % 3:
            n = n / 3

        return True if n == 1 else False
