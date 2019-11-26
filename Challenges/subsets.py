"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        
        def dfs(nums, seen):
            if len(seen)>=0:
                self.result.append(seen)
            for i in range(len(nums)):
                dfs(nums[i+1:], seen+[nums[i]])
                
        dfs(nums, [])
        return self.result


"""
Subsets

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

"""
DFS

# factorial time
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def backtracking(nums, curr):
            res.append(curr)
            for idx, n in enumerate(nums):
                backtracking(nums[idx+1:], curr + [n])
             
        backtracking(nums, [])
        return res
    
# Iteratively
def subsets(self, nums):
    res = [[]]
    for num in sorted(nums):
        res += [item+[num] for item in res]
    return res
