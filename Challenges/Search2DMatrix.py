"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""

"""
Time: O(n+m)
The key to the time complexity analysis is noticing that, on every iteration (during which we do not return true) either row or col is is decremented/incremented exactly once. Because row can only be decremented m times and col can only be incremented n times before causing the while loop to terminate, the loop cannot run for more than n+m iterations. Because all other work is constant, the overall time complexity is linear in the sum of the dimensions of the matrix.

Space: O(1) as we onlu use pointers

Other approach: Binary search on each row
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not len(matrix) or not len(matrix[0]):
            return False
        
        h, w = len(matrix), len(matrix[0])
        
        i = h-1
        j = 0
        
        while j < w and i >= 0:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True
        return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not len(matrix[0]):
            return False
        h = 0
        w = len(matrix[0])-1
        while 0 <= h < len(matrix) and 0 <= w < len(matrix[0]):
            if target == matrix[h][w]:
                return True
            if target > matrix[h][w]:
                h += 1
            elif target < matrix[h][w]:
                w -= 1
        return False
