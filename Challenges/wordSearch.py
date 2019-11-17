"""
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

"""
DFS at each point and use or to check if one of them passes
Time: O(n!)
Space: O(n^2)
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            res = dfs(board, i+1, j, word[1:]) or dfs(board, i-1, j, word[1:]) or dfs(board, i, j-1, word[1:]) or dfs(board, i, j+1, word[1:])
            board[i][j] = temp
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False

    
                    

