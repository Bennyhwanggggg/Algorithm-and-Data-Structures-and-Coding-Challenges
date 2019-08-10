"""
Longest Increasing Path In A Matrix

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

"""
DFS With Memo
Time: O(MN) without Memo it bt is O(2^(M+N))
Space: O(MN)
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.res = 0
        self.memo = dict()
        def dfs(i, j, prev):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] <= prev:
                return 0
            if (i, j) in self.memo:
                return self.memo[(i, j)]
            
            curr = 1 + max(dfs(i+1, j, matrix[i][j]), dfs(i-1, j, matrix[i][j]), dfs(i, j+1, matrix[i][j]), dfs(i, j-1, matrix[i][j]))
            
            self.res = max(self.res, curr)
            self.memo[(i, j)] = curr
            return curr
                    
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -float('inf'))

        return self.res

