"""
Count Servers that Communicate 

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.

 

Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""

"""
Solution Explanation
Iterate through grid and keep track of the counts of 1's that exist for each row and column.
Next, iterate through grid one more time and if it meets all of the following conditions then add it to the count variable that you will return:

The current cell has to have a value of 1
Either the row counts or the column counts are greater than 1 (which means two servers are communicating).
Time Complexity
O(n*m) (n=number of rows, m=number of cols)

Space Complexity
O(n+m) (n=number of rows, m=number of cols)
"""
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        count = 0
        rows_with_servers = [0] * len(grid)
        cols_with_servers = [0] * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows_with_servers[row] += 1
                    cols_with_servers[col] += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (rows_with_servers[row] > 1 or cols_with_servers[col] > 1):
                    count += 1
        return count

