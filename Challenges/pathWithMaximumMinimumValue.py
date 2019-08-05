"""
Path With Maximum Minimum Value
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

 Example 1:



Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:



Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:



Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
 

Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9
"""

"""
Notice that this is equivalent to:
remove all the cells with value below which that there is still a path from beginning to the end.


Since score is bounded by the smallest value in the path, the strategy would be always picking the neighboring cell with the largest value for the next step.
So we can use a priority queue to take all neighboring cells as candidates for the next step. And each time we pop out the largest one to move forward and update score as well.
And I set "seen" cell to -1 to avoid revisiting.
Once we detect the destination as one of the neighboring cells, we finish the path and return the score.

Time: (MNlog(N))
Space: O(MN)
"""
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        m, n = len(A), len(A[0])
        pq = [(-A[0][0], 0, 0)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        while pq:
            t, x, y = heapq.heappop(pq)
            if x == m-1 and y == n-1:
                return -t
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx and nx <= m-1 and 0 <= ny and ny <= n-1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(pq, (max(t, -A[nx][ny]), nx, ny))

