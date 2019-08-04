"""
Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

"""
Time: O((n+k)!)
Space: O(m)
"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(nums, curr, remain, res):
            if remain == 0:
                curr.sort()
                if curr not in res:
                    res.append(curr)
            
            for idx, num in enumerate(nums):
                if remain - num >= 0:
                    backtrack(nums, curr + [num], remain - num, res)
        
        
        backtrack(candidates, [], target, res)
        return res


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
