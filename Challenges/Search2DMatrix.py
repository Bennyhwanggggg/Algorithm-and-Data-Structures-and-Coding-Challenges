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