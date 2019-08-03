"""
Toeplitz Matrix
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].

Follow up:

What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
"""
Brute Force?
Time: O(MN)
Space: O(1)
"""
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        for i in range(len(matrix)):
            if not self.check(matrix, i, 0, matrix[i][0]):
                return False
        
        for j in range(1, len(matrix[0])):
            if not self.check(matrix, 0, j, matrix[0][j]):
                return False
        
        return True
            
    def check(self, matrix, i, j, val):
        while i < len(matrix) and j < len(matrix[0]):
            if matrix[i][j] != val:
                return False
            i += 1
            j += 1
        return True
    
"""
Intuition and Algorithm

We ask what feature makes two coordinates (r1, c1) and (r2, c2) belong to the same diagonal?

It turns out two coordinates are on the same diagonal if and only if r1 - c1 == r2 - c2.

This leads to the following idea: remember the value of that diagonal as groups[r-c]. If we see a mismatch, the matrix is not Toeplitz; otherwise it is.

Time: O(MN)
Space: O(1)
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True

