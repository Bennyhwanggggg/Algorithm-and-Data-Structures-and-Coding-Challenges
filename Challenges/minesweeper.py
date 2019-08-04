"""
Minesweeper

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.
 

Example 1:

Input: 

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output: 

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
"""

"""
Time: O(MN)
Space: O(1)
"""
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.m, self.n = len(board), len(board[0])
        self.board = board
        if not self.m or not self.n:
            return self.board
        i, j = click
        if self.board[i][j] == 'M':  # If a mine ('M') is revealed, then the game is over - change it to 'X'.
            self.board[i][j] = 'X'
            return self.board
        # run dfs to reveal the board
        self.dfs(i, j)
        return self.board
    
    def dfs(self, i, j):
        if self.board[i][j] != 'E':  # if cell is not unrevealed empty, don't need to do anything
            return
    
        directions = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]
        
        # Find number of mines
        mine_count = 0
        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < self.m and 0 <= nj < self.n and self.board[ni][nj] == 'M':        
                mine_count += 1
                
        if mine_count == 0:
            self.board[i][j] = 'B'
        else:
            self.board[i][j] = str(mine_count)
            return

        for d in directions:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < self.m and 0 <= nj < self.n:
                self.dfs(ni, nj)

