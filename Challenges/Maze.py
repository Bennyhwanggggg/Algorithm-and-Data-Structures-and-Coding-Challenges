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
