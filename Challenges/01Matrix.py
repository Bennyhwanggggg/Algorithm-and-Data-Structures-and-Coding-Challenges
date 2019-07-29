"""
01 Matrix

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]
 

Note:

The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""

"""
Intuition

A better brute force: Looking over the entire matrix appears wasteful and hence, we can use Breadth First Search(BFS) to limit the search to the nearest 0 found for each 1. As soon as a 0 appears during the BFS, we know that the 0 is nearest, and hence, we move to the next 1.

Think again: But, in this approach, we will only be able to update the distance of one 1 using one BFS, which could in fact, result in slightly higher complexity than the Approach #1 brute force. But hey,this could be optimised if we start the BFS from 0s and thereby, updating the distances of all the 1s in the path.

Algorithm

For our BFS routine, we keep a queue, q to maintain the queue of cells to be examined next.
We start by adding all the cells with 0s to q.
Intially, distance for each 0 cell is 0 and distance for each 1 is INT_MAX, which is updated during the BFS.
Pop the cell from queue, and examine its neighbours. If the new calculated distance for neighbour {i,j} is smaller, we add {i,j} to q and update dist[i][j].

Time: O(mn)
Space: O(mn)
"""

class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        h = len(matrix)
        w = len(matrix[0])
        
        queue = []
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    queue.append((i,j))
                else:
                    matrix[i][j] = float("inf")
            
        for row, col in queue:
            dist = matrix[row][col] + 1
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = row + dy;
                c = col + dx;
                if 0 <= r < h and 0 <= c < w and dist < matrix[r][c]:
                    matrix[r][c] = dist
                    queue.append((r,c))
                    
        return matrix
                    
"""
DP

Intuition

The distance of a cell from 0 can be calculated if we know the nearest distance for all the neighbours, in which case the distance is minimum distance of any neightbour + 1. And, instantly, the word come to mind DP!!
For each 1, the minimum path to 0 can be in any direction. So, we need to check all the 4 direction. In one iteration from top to bottom, we can check left and top directions, and we need another iteration from bottom to top to check for right and bottom direction.

Algorithm

Iterate the matrix from top to bottom-left to right:
Update dist[i][j]=min(dist[i][j],min(dist[i][j−1],dist[i−1][j])+1) i.e., minimum of the current dist and distance from top or left neighbour +1, that would have been already calculated previously in the current iteration.
Now, we need to do the back iteration in the similar manner: from bottom to top-right to left:
Update dist[i][j]=min(dist[i][j],min(dist[i][j+1],dist[i+1][j])+1) i.e. minimum of current dist and distances calculated from bottom and right neighbours, that would be already available in current iteration.

We simply do 2 iterations from first to last and last to first element.
For the 1st for loop, we update distance of element with minimum of previous top and left elements + 1 (itself).
For the 2nd for loop, we update distance of element with minimum of previous bottom and right elements + 1 (itself).
As a result, we get minimum distance value for each element updated with distances of neighbours + 1.
"""
class Solution:
    def updateMatrix(self, matrix):
        m, n = len(matrix), len(matrix and matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = float("inf")
                    if i > 0 and matrix[i - 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i - 1][j] + 1
                    if j > 0 and matrix[i][j - 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j - 1] + 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] != 0:
                    if i + 1 < m and matrix[i + 1][j] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i + 1][j] + 1
                    if j + 1 < n and matrix[i][j + 1] + 1 < matrix[i][j]:
                        matrix[i][j] = matrix[i][j + 1] + 1
        return matrix
        
        
