"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        def findParameter(grid, i, j):
            parameter = 4
            if i > 0 and grid[i-1][j] == 1:
                parameter -= 1
            if i < len(grid)-1 and grid[i+1][j]:
                parameter -= 1
            if j > 0 and grid[i][j-1] == 1:
                parameter -= 1
            if j < len(grid[0])-1 and grid[i][j+1]:
                parameter -= 1
            return parameter
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    res += findParameter(grid, i, j)
        return res

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def checkNeighbours(grid, i, j):
            count = 4
            for n in range(-1, 2, 2):
                if 0 <= i + n < len(grid) and grid[i + n][j]:
                    count -= 1
                if 0 <= j + n < len(grid[0]) and grid[i][j + n]:
                    count -= 1
            return count

        p = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]:
                    p += checkNeighbours(grid, row, col)
        return p
