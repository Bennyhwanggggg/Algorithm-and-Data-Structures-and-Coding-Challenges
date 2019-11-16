"""
Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

 

Example:

Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""

"""
The overall workflow of the algorithm is intuitive, which consists of a loop over each cell in the board and a recursive function call starting from the cell. Here is the skeleton of the algorithm.

We build a Trie out of the words in the dictionary, which would be used for the matching process later.

Starting from each cell, we start the backtracking exploration (i.e. backtracking(cell)), if there exists any word in the dictionary that starts with the letter in the cell.

During the recursive function call backtracking(cell), we explore the neighbor cells (i.e. neighborCell) around the current cell for the next recursive call backtracking(neighborCell). At each call, we check if the sequence of letters that we traverse so far matches any word in the dictionary, with the help of the Trie data structure that we built at the beginning.
"""

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        KEY = '$'
        
        trie = dict()
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, dict())
            node[KEY] = word
            
        rowNum, colNum = len(board), len(board[0])
        
        res = []
        
        def backtracking(row, col, parent):
            letter = board[row][col]
            currNode = parent[letter]
            
            wordMatch = currNode.pop(KEY, False)
            if wordMatch:
                res.append(wordMatch)
            
            board[row][col] = '#'
            
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nR, nC = row + dr, col + dc
                if 0 <= nR < rowNum and 0 <= nC < colNum:
                    if board[nR][nC] in currNode:
                        backtracking(nR, nC, currNode)  
            
            board[row][col] = letter
        
        for i in range(rowNum):
            for j in range(colNum):
                if board[i][j] in trie:
                    backtracking(i, j, trie)
        return res


class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = {}
        for word in words:
            t = trie
            for char in word:
                if char not in t:
                    t[char] = {}
                t = t[char]
            t['#'] = '#'
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.find(board, row, col, trie, '')
        return list(self.res)

    def find(self, board, i, j, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.find(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
            self.find(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
            self.find(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
            self.find(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
            self.used[i][j] = False
