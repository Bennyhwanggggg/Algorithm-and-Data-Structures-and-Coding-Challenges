class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        skip = [[i for i in [0] * 10] for j in range(11)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[6][4] = skip[4][6] = 5

        visited = [False] * 10

        res = 0

        def DFS(visited, skip, curr, remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            visited[curr] = True
            result = 0
            for i in range(1, 10):
                if not visited[i] and (skip[curr][i] == 0 or visited[skip[curr][i]]):
                    result += DFS(visited, skip, i, remain - 1)
            visited[curr] = False
            return result

        for i in range(m, n + 1):
            # Recognize that it is symmetric
            res += DFS(visited, skip, 1, i - 1) * 4
            res += DFS(visited, skip, 2, i - 1) * 4
            res += DFS(visited, skip, 5, i - 1)
        return res

