class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1, 10)]

        def dfs(res, k, candid, curr_sum, line, start):
            if curr_sum == 0 and len(line) == k:
                res.append(copy.deepcopy(line))
                return
            for i in range(start, len(candid)):
                if curr_sum - candid[i] < 0:
                    break
                line.append(candid[i])
                dfs(res, k, candid, curr_sum - candid[i], line, i + 1)
                line.pop()

        res = []
        dfs(res, k, nums, n, [], 0)
        return res