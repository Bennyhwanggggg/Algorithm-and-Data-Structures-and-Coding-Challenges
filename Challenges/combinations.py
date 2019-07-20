"""
Combinations

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

"""
Backtracking

Here is a backtrack function which takes a first integer to add and a current combination as arguments backtrack(first, curr).

If the current combination is done - add it to output.

Iterate over the integers from first to n.

Add integer i into the current combination curr.

Proceed to add more integers into the combination : backtrack(i + 1, curr).

Backtrack by removing i from curr.

Time: O(Total number combination based on k chose n)
Space: Same as time
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        
        def backtrack(nums, curr, result):
            if len(curr) == k:
                result.append(curr)
            
            for i, x in enumerate(nums):
                backtrack(nums[i+1:], curr + [x], result)
        
        result = []
        backtrack(nums, [], result)
        return result
    
"""
Another approach using Lexicographic combination

The algorithm is quite straightforward :

Initiate nums as a list of integers from 1 to k. Add n + 1 as a last element, it will serve as a sentinel. Set the pointer in the beginning of the list j = 0.

While j < k :

Add the first k elements from nums into the output, i.e. all elements but the sentinel.

Find the first number in nums such that nums[j] + 1 != nums[j + 1] and increase it by one nums[j]++ to move to the next combination.
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        
        output, j = [], 0
        while j < k:
            # add current combination
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1
            
        return output


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        stack = [(0, [])]
        res = []
        while stack:
            cur, path = stack.pop()
            if len(path) == k:
                res.append(path)    
            if cur < n:
                stack.extend([(i, path+[i]) for i in range(cur+1, n+1) if len(path) < k])
        return res


# recursive
class Solution2(object):
    def getCombine(self, n, k, index, prev, ans):
        if len(prev)==k:
            ans.append(prev)
            return
        for i in range(index,n-(k-len(prev))+2):
            self.getCombine(n, k, i+1, prev+[i], ans)

    def combine(self, n, k):
        ans = []
        if k <= n:
            self.getCombine(n, k, 1, [], ans)
        return ans
