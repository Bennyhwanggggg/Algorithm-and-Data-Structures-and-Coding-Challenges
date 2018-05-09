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

