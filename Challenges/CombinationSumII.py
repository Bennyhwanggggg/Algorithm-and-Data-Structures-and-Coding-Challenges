class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        stack = [[[], 0, 0]]  # current numset, current sum, ind
        res = []
        visited = set()

        while stack:
            nums, curr_sum, ind = stack.pop()
            if curr_sum == target:
                res.append(nums)
                continue
            for i in range(ind, len(candidates)):
                if curr_sum + candidates[i] <= target and tuple(nums + [candidates[i]]) not in visited:
                    stack.append([nums + [candidates[i]], curr_sum + candidates[i], i + 1])
                    visited.add(tuple(nums + [candidates[i]]))
        return res

#         ans = []
#         def dfs(candidates, tar, nums, start, ans):
#             if tar == 0:
#                 ans.append(copy.deepcopy(nums))
#                 return
#             for i in range(start, len(candidates)):
#                 if i != start and candidates[i] == candidates[i-1]:
#                     continue
#                 nums.append(candidates[i])
#                 dfs(candidates, tar-candidates[i], nums, i+1, ans)
#                 nums.pop()

#         candidates.sort()
#         dfs(candidates, target, [], 0, ans)
#         return ans
