"""
Unique Paths

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""

"""
DP (recursion is 2^n)
Time: O(m*n)
Space: O(m*n) => can be reduced to just storing one row to O(n) space
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(m)] for _ in range(n)]
        
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
    
"""
Math Way
"""
# math C(m+n-2,n-1)
def uniquePaths1(self, m, n):
    if not m or not n:
        return 0
    return math.factorial(m+n-2)/(math.factorial(n-1) * math.factorial(m-1))


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1 for i in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if not i or not j:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[n - 1][m - 1]
