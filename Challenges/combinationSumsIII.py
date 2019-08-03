"""
Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""

"""
Time O(10!)
Space: O(1)
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        def backtrack(nums, curr, res):
            if len(curr) == k and sum(curr) == n:
                res.append(curr)
            
            for idx, val in enumerate(nums):
                backtrack(nums[idx+1:], curr + [val], res)
        
        res = []
        backtrack([n for n in range(1, 10)], [], res)
        return res
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(comb, res, k, target, i):
            if len(comb) == k and target == 0:
                res.append(comb)
                return
            for j,x in enumerate(candidates[i:]):
                if x <= target:
                    target -= x
                    dfs(comb + [x], res, k, target, i+j+1)
                    target += x
        
        candidates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        res = []
        dfs([], res, k, n, 0)
        return res


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
