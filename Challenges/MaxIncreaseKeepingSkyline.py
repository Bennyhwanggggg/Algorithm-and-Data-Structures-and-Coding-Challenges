"""
In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.

Solution
Intuition and Algorithm

The skyline looking from the top is col_maxes = [max(column_0), max(column_1), ...]. Similarly, the skyline from the left is row_maxes [max(row_0), max(row_1), ...]

In particular, each building grid[r][c] could become height min(max(row_r), max(col_c)), and this is the largest such height. If it were larger, say grid[r][c] > max(row_r), then the part of the skyline row_maxes = [..., max(row_r), ...] would change.

These increases are also independent (none of them change the skyline), so we can perform them independently.
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # find the max of each column and row
        row_maxes = [max(row) for row in grid]
        # col_maxes = [max(col) for col in zip(*grid)]
        col_maxes = []
        for i in range(len(grid[0])):
            curr_max = 0
            for j in range(len(grid)):
                curr_max = max(grid[j][i], curr_max)
            col_maxes.append(curr_max)
        return sum(min(row_maxes[r], col_maxes[c]) - val 
                   for r, row in enumerate(grid) 
                   for c, val in enumerate(row))
