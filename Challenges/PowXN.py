class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n < 1:
            return 1 / (self.myPow(x, -n))
        if n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n / 2)