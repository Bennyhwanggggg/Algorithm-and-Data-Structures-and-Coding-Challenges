class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix or not matrix[0]:
            return []

        spiral = []

        m, n = len(matrix), len(matrix[0])

        u, d, l, r = 0, m - 1, 0, n - 1

        while u < d and l < r:
            spiral.extend([matrix[u][j] for j in range(l, r)])
            spiral.extend([matrix[j][r] for j in range(u, d)])
            spiral.extend([matrix[d][j] for j in range(r, l, -1)])
            spiral.extend([matrix[j][l] for j in range(d, u, -1)])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1

        if l == r:
            spiral.extend([matrix[j][l] for j in range(u, d + 1)])
        elif u == d:
            spiral.extend([matrix[u][j] for j in range(l, r + 1)])

        return spiral