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
