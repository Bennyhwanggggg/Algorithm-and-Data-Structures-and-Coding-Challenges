class Solution:
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        #         def dfs(M, pos, count, d):
        #             x, y = pos
        #             r, c = d
        #             # M[x][y] = '@'
        #             #print(M)
        #             newx, newy = x+r, c+y
        #             #print(newx, newy)
        #             if len(M) > newx >= 0 and len(M[0]) > newy >= 0 and M[newx][newy] != 0:
        #                 #print('here', count)
        #                 return dfs(M, (newx, newy), count + 1, d)
        #             return count

        #         consec = 0
        #         dirs = [(1, 0), (0, 1), (1, 1), (1, -1)]
        #         for row in range(len(M)):
        #             for col in range(len(M[0])):
        #                 if M[row][col] == 1:
        #                     for d in dirs:
        #                         consec = max(dfs(M, (row, col), 1, d), consec)
        #         return consec
        maxlen = 0
        currlen = collections.Counter()
        for i, row in enumerate(M):
            for j, a in enumerate(row):
                for key in i, j + .1, i + j + .2, i - j + .3:
                    currlen[key] = (currlen[key] + 1) * a
                    maxlen = max(maxlen, currlen[key])
        return maxlen
