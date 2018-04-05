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
