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
