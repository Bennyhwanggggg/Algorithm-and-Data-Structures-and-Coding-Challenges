"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        results = {}
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s = i + j
                if s not in results:
                    results[s] = [matrix[i][j]]
                else:
                    results[s].append(matrix[i][j])

        for i in [int(n) for n in results.keys()]:
            if not i % 2:
                res.extend([i for i in reversed(results[i])])
            else:
                res.extend(results[i])
        return res


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not len(matrix) or not len(matrix[0]):
            return []
        
        results = collections.defaultdict(list)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                s = i + j
                results[s].append(matrix[i][j])
                
        ans = []
        for i in results.keys():
            if not i%2:
                ans.extend(results[i][::-1])
            else:
                ans.extend(results[i])
        return ans
