class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for row in range(m):
            for col in range(n):
                if not row and not col:
                    continue
                elif not row:
                    grid[row][col] += grid[row][col-1]
                elif not col:
                    grid[row][col] += grid[row-1][col]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
        return grid[m-1][n-1]