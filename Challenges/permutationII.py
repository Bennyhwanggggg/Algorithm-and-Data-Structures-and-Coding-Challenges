"""
Permutations II (Permutations without duplicates)

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

"""
Time: O(n!) when no duplicates
Space: O(n!) stack space
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, permutation, result):
            if not len(nums):
                result.append(permutation)
            for i, x in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:], permutation+[x], result)
        
        nums.sort()  # sort to group duplicates
        result = []
        backtrack(nums, [], result)
        return result
