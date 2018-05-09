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
