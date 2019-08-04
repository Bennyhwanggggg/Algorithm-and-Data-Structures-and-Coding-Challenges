"""
Pacific Atlantic Water Flow

Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""

"""
Time: O(MN)
Space: O(MN)
"""
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if not matrix: 
            return []
        
        m, n = len(matrix), len(matrix[0])
        p_visited = [[False for _ in range(n)] for _ in range(m)]
        a_visited = [[False for _ in range(n)] for _ in range(m)]
        result = []
        
        for i in range(m):
            self.dfs(matrix, i, 0, p_visited)
            self.dfs(matrix, i, n-1, a_visited)
        
        for j in range(n):
            self.dfs(matrix, 0, j, p_visited)
            self.dfs(matrix, m-1, j, a_visited)
            
        for i in range(m):
            for j in range(n):
                if p_visited[i][j] and a_visited[i][j]:
                    result.append([i, j])
        return result
            
            
    def dfs(self, matrix, i, j, visited):
        visited[i][j] = True
        for di, dj in self.directions:
            x, y = i+di, j+dj
            if 0 <= x and x < len(matrix) and 0 <= y and y < len(matrix[0]) and not visited[x][y] and matrix[x][y] >= matrix[i][j]:
                self.dfs(matrix, x, y, visited)
                

