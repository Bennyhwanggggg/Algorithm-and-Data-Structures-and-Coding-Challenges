import math


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        def getSurroundingSum(M, i, j):
            sums = M[i][j]
            count = 1
            w = len(M[0])
            h = len(M)
            for r in range(-1, 2):
                if j + r >= 0 and j + r < w:
                    if i - 1 >= 0:
                        sums += M[i - 1][j + r]
                        count += 1
                    if i + 1 < h:
                        sums += M[i + 1][j + r]
                        count += 1

            if j - 1 >= 0:
                sums += M[i][j - 1]
                count += 1
            if j + 1 < w:
                sums += M[i][j + 1]
                count += 1
            return int(math.floor(sums / count))

        w = len(M[0])
        h = len(M)
        color = {}
        for row in range(h):
            for col in range(w):
                color[(row, col)] = getSurroundingSum(M, row, col)
        for row in range(h):
            for col in range(w):
                M[row][col] = color[(row, col)]

        return M
