class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        def dfsComponents(start, curId):
            starti, startj = start
            grid[starti][startj] = False
            if starti > 0 and grid[starti - 1][startj] == "1":
                dfsComponents((starti - 1, startj), curId)
            if starti < nrows - 1 and grid[starti + 1][startj] == "1":
                dfsComponents((starti + 1, startj), curId)
            if startj > 0 and grid[starti][startj - 1] == "1":
                dfsComponents((starti, startj - 1), curId)
            if startj < ncols - 1 and grid[starti][startj + 1] == "1":
                dfsComponents((starti, startj + 1), curId)

        if not grid:
            return 0
        nrows = len(grid)
        ncols = len(grid[0])
        id = 0
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] == "1":
                    dfsComponents((i, j), id)
                    id += 1

        return id


