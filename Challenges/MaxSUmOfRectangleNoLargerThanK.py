class Solution:

    def findMaxArea(self, a, l, r, k):
        if l >= r: return -2 ** 31

        m = (l + r) // 2

        res = max(self.findMaxArea(a, l, m, k), self.findMaxArea(a, m + 1, r, k))

        i = l
        for j in range(m + 1, r + 1):
            while i <= m and a[j] - a[i] > k: i += 1
            if i > m: break
            if res < a[j] - a[i]: res = a[j] - a[i]

        tmp = [0] * (r - l + 1)
        i = l
        j = m + 1
        t = 0

        while i <= m and j <= r:
            if a[i] <= a[j]:
                tmp[t] = a[i]
                i += 1
                t += 1
            else:
                tmp[t] = a[j]
                t += 1
                j += 1

        while i <= m:
            tmp[t] = a[i]
            t += 1
            i += 1

        while j <= r:
            tmp[t] = a[j]
            t += 1
            j += 1

        for i in range(len(tmp)): a[l + i] = tmp[i]

        return res

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        m = len(matrix)
        n = len(matrix[0])
        if m > n:
            m, n = n, m
            a = [[0] * n for i in range(m)]

            for i in range(m):
                for j in range(n):
                    a[i][j] = matrix[j][i]

        else:
            a = [[0] * n for i in range(m)]
            for i in range(m):
                for j in range(n):
                    a[i][j] = matrix[i][j]

        res = -2 ** 31
        for i in range(m):
            h = [0] * n
            for j in range(i, m):
                sum = [0] * (n + 1)

                low = 0
                maxArea = -2 ** 31

                for t in range(n):
                    h[t] += a[j][t]
                    sum[t + 1] = sum[t] + h[t]

                    maxArea = max(maxArea, sum[t + 1] - low)
                    low = min(low, sum[t + 1])

                if maxArea <= res: continue

                if maxArea == k: return k
                if maxArea > k: maxArea = self.findMaxArea(sum, 0, n, k)

                res = max(res, maxArea)

        return res