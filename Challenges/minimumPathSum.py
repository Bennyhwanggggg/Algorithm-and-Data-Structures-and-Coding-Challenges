"""
Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

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
