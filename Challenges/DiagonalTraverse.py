class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        results = {}
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s = i + j
                if s not in results:
                    results[s] = [matrix[i][j]]
                else:
                    results[s].append(matrix[i][j])

        for i in [int(n) for n in results.keys()]:
            if not i % 2:
                res.extend([i for i in reversed(results[i])])
            else:
                res.extend(results[i])
        return res