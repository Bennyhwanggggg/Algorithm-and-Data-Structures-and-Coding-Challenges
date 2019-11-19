"""
Kth Smallest Element in a Sorted Matrix

Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
"""

"""
Sorting
Time: O(N^2log(N))
Space: O(N^2)

can also use heap which is O(k(log(N))) and O(k) space
"""
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        res = []
        for mat in matrix:
            res.extend(mat)
        res.sort()
        return res[k-1]

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix or not len(matrix[0]):
            return matrix[-1][-1]

        nums = []
        for row in matrix:
            nums.extend(row)

        return sorted(nums)[k - 1]

