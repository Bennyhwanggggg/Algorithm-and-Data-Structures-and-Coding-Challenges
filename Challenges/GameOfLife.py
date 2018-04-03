class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        # check neighbours
        def getneighbours(board, i, j):
            count = 0
            for r in range(-1, 2):
                if j + r >= 0 and j + r < len(board[0]):
                    if i - 1 >= 0:
                        count += board[i - 1][j + r]
                    if i + 1 < len(board):
                        count += board[i + 1][j + r]
            if j - 1 >= 0:
                count += board[i][j - 1]
            if j + 1 < len(board[0]):
                count += board[i][j + 1]
            return count

        mapper = {}

        for row in range(len(board)):
            for col in range(len(board[0])):
                n = getneighbours(board, row, col)
                mapper[(row, col)] = n

        for row in range(len(board)):
            for col in range(len(board[0])):
                if mapper[(row, col)] < 2 and board[row][col]:
                    board[row][col] = 0
                if mapper[(row, col)] == 3 and not board[row][col]:
                    board[row][col] = 1
                if mapper[(row, col)] > 3 and board[row][col]:
                    board[row][col] = 0