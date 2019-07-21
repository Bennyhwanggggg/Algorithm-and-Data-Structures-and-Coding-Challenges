"""
Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""



"""
DFS
Time: O(MN)
Space: O(MN)
"""

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea, self.area= 0,0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    self.getArea(grid,(x,y))
                    maxArea = max(maxArea,self.area)
                    self.area=0
        return maxArea
                    
    def getArea(self,grid,point):
        self.area+=1
        x,y = point
        grid[x][y]=0
        for u,v in [(1,0),(-1,0),(0,1),(0,-1)]:
            if x+u >= 0 and x+u  < len(grid):
                if y+v >= 0 and y+v < len(grid[0]):
                    if grid[x+u][y+v]==1:
                        self.getArea(grid,(x+u,y+v))


# iterative
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # DFS
        if len(grid) == 0:
            return 0
        height = len(grid)
        width = len(grid[0])
        visit = set()
        max_area = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1 and (i,j) not in visit:
                    visit.add((i,j))
                    stack = [(i,j)]
                    area = 1
                    while stack:
                        u = stack.pop()
                        i,j = u[0],u[1]
                        if i > 0 and grid[i-1][j] == 1 and (i-1,j) not in visit:
                            stack.append((i-1,j))
                            visit.add((i-1,j))
                            area += 1
                        if i < height - 1 and grid[i+1][j] == 1 and (i+1,j) not in visit:
                            stack.append((i+1,j))
                            visit.add((i+1,j))
                            area += 1
                        if j > 0 and grid[i][j-1] == 1 and (i,j-1) not in visit:
                            stack.append((i,j-1))
                            visit.add((i,j-1))
                            area += 1
                        if j < width - 1 and grid[i][j+1] == 1 and (i,j+1) not in visit:
                            stack.append((i,j+1))
                            visit.add((i,j+1))
                            area += 1
                    if area > max_area:
                        max_area = area
        return max_area
