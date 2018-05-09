class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n:
            return False
        while not n%2:
            n /= 2
        return True if n==1 else False