"""
Triangle

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

"""
Time: O(N) N = number of values in triangle
Space: O(N)
"""
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for idx, row in enumerate(triangle):
            if idx == 0:
                continue
            for i, val in enumerate(row):
                if i == len(row)-1:
                    row[i] += triangle[idx-1][i-1]
                elif i == 0:
                    row[i] += triangle[idx-1][i]
                else:
                    row[i] += min(triangle[idx-1][i], triangle[idx-1][i-1])
            
        return min(triangle[-1])

