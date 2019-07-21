"""
The Maze

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
"""

"""
BFS
Time: O(mn)
Space: O(mn)
"""
class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        queue = collections.deque([(start[0], start[1])])
        visited[start[0]][start[1]] = True
        
        while queue:
            curr_x, curr_y = queue.popleft()
            visited[curr_x][curr_y] = True
            if curr_x == destination[0] and curr_y == destination[1]:
                return True
            for direction in directions:
                x = curr_x + direction[0]
                y = curr_y + direction[1]
                while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 0:
                    x += direction[0]
                    y += direction[1]
                if not visited[x-direction[0]][y-direction[1]]:
                    queue.append((x-direction[0], y-direction[1]))
        
        return False
        
        

import collections


class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        queue = collections.deque()
        queue.append(start)
        while queue:
            x, y = queue.popleft()
            maze[x][y] = 2
            if x == destination[0] and y == destination[1]:
                return True
            for i, j in directions:
                row = i + x
                col = j + y
                while len(maze) > row >= 0 and len(maze[0]) > col >= 0 and maze[row][col] != 1:
                    row += i
                    col += j
                row -= i
                col -= j
                if not maze[row][col]:
                    queue.append([row, col])
        return False
