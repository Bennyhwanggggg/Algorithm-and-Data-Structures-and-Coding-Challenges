"""
Given an 2D board, count how many battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:
You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
"""

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def dfs(i, j):
            board[i][j] = '.'
            if i-1 >= 0 and board[i-1][j] == 'X':
                dfs(i-1, j)
            if i+1 < len(board) and board[i+1][j] == 'X':
                dfs(i+1, j)
            if j-1 >= 0 and board[i][j-1] == 'X':
                dfs(i, j-1)
            if j+1 < len(board[0]) and board[i][j+1] == 'X':
                dfs(i, j+1)
        
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    dfs(i, j)
                    count += 1
        return count
                    
