class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.rec(n, 0)

    def rec(self, n, steps):
        if n <= 1:
            return steps
        if not n % 2:
            return self.rec(n // 2, steps + 1)
        else:
            return min(self.rec(n + 1, steps + 1), self.rec(n - 1, steps + 1))

