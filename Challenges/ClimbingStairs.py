class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(n, {})

    def helper(self, n, memo):
        if n in memo:
            return memo[n]
        if n == 0:
            return 1
        if n < 0:
            return 0
        memo[n] = self.helper(n - 1, memo) + self.helper(n - 2, memo)
        return memo[n]
