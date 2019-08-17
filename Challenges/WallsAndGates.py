"""
Walls and Gates

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
"""
BFS from each source
Time: O(MN)
Space: O(MN) every node into queue
"""
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms:
            return
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    queue = collections.deque()
                    visited = set()
                    for di, dj in directions:
                        queue.append((i+di, j+dj, 1))
                    while queue:
                        x, y, val = queue.popleft()
                        if x < 0 or x > len(rooms)-1 or y < 0 or y > len(rooms[0])-1 or rooms[x][y] <= 0 or (x, y) in visited:
                            continue
                        rooms[x][y] = min(rooms[x][y], val)
                        visited.add((x, y))
                        for di, dj in directions:
                            queue.append((x+di, y+dj, val+1))
        
        
                



class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """

        queue = collections.deque()
        grid = rooms[:]
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0:
                    queue.append([(row, col), 0])

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        while queue:
            pos, step = queue.popleft()
            i, j = pos
            rooms[i][j] = min(step, rooms[i][j])
            for x, y in directions:
                if len(rooms) > x + i >= 0 and len(rooms[0]) > y + j >= 0 and rooms[x + i][y + j] >= step + 1:
                    if rooms[x + i][y + j] != 0 and rooms[x + i][y + j] != -1:
                        queue.append([(x + i, y + j), step + 1])
        # for row in range(len(rooms)):
        #     for col in range(len(rooms[0])):
        #         if rooms[row][col] == 2147483647:
        #             rooms[row][col] = 'INF'
