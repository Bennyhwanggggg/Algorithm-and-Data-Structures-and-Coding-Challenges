"""
Bomb Enemy

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
Note: You can only put the bomb at an empty cell.

Example:

Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
Output: 3 
Explanation: For the given grid,

0 E 0 0 
E 0 W E 
0 E 0 0

Placing a bomb at (1,1) kills 3 enemies.
"""

"""
Brute Force
Time: O((mn)*(m+n))
Space: O(1)
"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    count = 0
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        while 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] != 'W':
                            if grid[ni][nj] == 'E':
                                count += 1
                            ni += di
                            nj += dj
                    res = max(res, count)
        
        return res
    
"""
DP
Time: O(mn)
Space: O(mn)
We can optimize on this by doing 4 passes and adding the number of E's seen so far, and reset if we see a 'W'.
From left to right then right to left for E's seen in each row. And then from up to down and down to up for each E seen so far in column.
"""
class Solution(object):
    def maxKilledEnemies(self, grid):
        if len(grid) == 0:
            return 0
        max_hits = 0
        nums = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        
        #From Left
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    row_hits += 1
                elif grid[i][j] == 'W':
                    row_hits = 0
                else:
                    nums[i][j] = row_hits
                
        #From Right
        for i in range(len(grid)):
            row_hits = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'W':
                    row_hits = 0
                elif grid[i][j] == 'E':
                    row_hits +=1
                else:
                    nums[i][j] += row_hits

        # up -> down
        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)):
                if grid[col][i] == 'E':
                    col_hits += 1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits

        for i in range(len(nums[0])):
            col_hits = 0
            for col in range(len(nums)-1, -1, -1):
                if grid[col][i] == 'E':
                    col_hits +=1
                elif grid[col][i] == 'W':
                    col_hits = 0
                else:
                    nums[col][i] += col_hits
                    max_hits = max(max_hits, nums[col][i])


        return max_hits

