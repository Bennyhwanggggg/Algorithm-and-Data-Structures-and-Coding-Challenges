"""
Permutation

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

If the first integer to consider has index n that means that the current permutation is done.
Iterate over the integers from index first to index n - 1.
Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
Now backtrack, i.e. swap(nums[first], nums[i]) back.

Time: O(n!)
Space: O(n!) recursion space
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(nums, permutation, result):
            if not len(nums):
                result.append(permutation)
            for i, x in enumerate(nums):
                backtrack(nums[:i]+nums[i+1:], permutation + [x], result)
        
        result = []
        backtrack(nums, [], result)
        return result
