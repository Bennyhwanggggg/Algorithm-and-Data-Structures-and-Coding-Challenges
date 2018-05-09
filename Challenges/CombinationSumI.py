class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def dfs(res, candidates, current_sum, line, start):
            if current_sum == 0:
                res.append(copy.deepcopy(line))
                return
            for i in range(start, len(candidates)):
                if current_sum - candidates[i] < 0:
                    break
                line.append(candidates[i])
                dfs(res, candidates, current_sum - candidates[i], line, i)
                line.pop()

        res = []
        candidates.sort()
        dfs(res, candidates, target, [], 0)
        return res