"""
Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

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

"""
Backtracking

Time: O(2^n)
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(nums, curr, remain, res):
            if remain == 0:
                res.add(tuple(curr))
                return
            for idx, num in enumerate(nums):
                if idx > 0 and nums == nums[idx-1]:
                    continue
                if remain - num < 0:
                    break
                backtrack(nums[idx+1:], curr + [num], remain-num, res)
        
        res = set()
        candidates.sort()
        backtrack(candidates, [], target, res)
        return [list(sol) for sol in res]

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(nums, curr, remain, res):
            if remain == 0:
                res.append(curr)
                return
            for idx, num in enumerate(nums):
                if idx > 0 and num == nums[idx-1]:
                    continue
                if remain - num < 0:
                    break
                backtrack(nums[idx+1:], curr + [num], remain-num, res)
        
        res = []
        candidates.sort()
        backtrack(candidates, [], target, res)
        return res
