"""
DFS
Time: O(M X N)
Space: O(MXN) if all grid is '1' and we do this many recursive calls.

FollowUp:
BFS uses less space

Union Find has same complexity as DFS
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            grid[i][j] = '0'
            if i > 0 and grid[i-1][j] == '1':
                dfs(i-1, j)
            if i < len(grid)-1 and grid[i+1][j] == '1':
                dfs(i+1, j)
            if j > 0 and grid[i][j-1] == '1':
                dfs(i, j-1)
            if j < len(grid[0])-1 and grid[i][j+1] == '1':
                dfs(i, j+1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count

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


