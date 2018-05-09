class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        m = len(matrix)
        n = len(matrix[0])
        row, col = False, False
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
                    if not i:
                        row = True
                    if not j:
                        col = True

        for i in range(1, m):
            if not matrix[i][0]:
                for j in range(1, n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if not matrix[0][j]:
                for i in range(1, m):
                    matrix[i][j] = 0
        if row:
            for j in range(n):
                matrix[0][j] = 0
        if col:
            for i in range(m):
                matrix[i][0] = 0



