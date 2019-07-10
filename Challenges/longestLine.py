"""
Given a 01 matrix M, find the longest line of consecutive one in the matrix. The line could be horizontal, vertical, diagonal or anti-diagonal.
Example:
Input:
[[0,1,1,0],
 [0,1,1,0],
 [0,0,0,1]]
Output: 3
Hint: The number of elements in the given matrix will not exceed 10,000.
"""

"""
DP:
Time: O(MN)
Space: O(3MN)
"""
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        m = len(M)
        n = len(M[0])
        
        res = 0
        
        dp = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
        
        
        for i in range(m):
            
            for j in range(n):
                if M[i][j] == 0:
                    for k in range(4):
                        dp[i][j][k] = 0
                    continue
                for k in range(4):
                    dp[i][j][k] = 1
                    
                if j > 0: # horizontal line
                    dp[i][j][0] += dp[i][j-1][0]
                if i > 0: # vertical line
                    dp[i][j][1] += dp[i-1][j][1]
                if j > 0 and i > 0: # diag
                    dp[i][j][2] += dp[i-1][j-1][2]
                if j < n - 1 and i > 0: # anti diag
                    dp[i][j][3] += dp[i-1][j+1][3]
                
                res = max(res, dp[i][j][0], dp[i][j][1], dp[i][j][2], dp[i][j][3])
                
        return res
                    
                    
                
                



"""
Brute force:
Time O(n^2)
Space O(1)
"""
class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        res = 0
        if not M:
            return res
        for i in range(len(M)):
            res = max(res, self.findMaxInRow(M, i)) 
            res = max(res, self.findMaxInDiag(M, i, 0)) # starts from left edge
            res = max(res, self.findMaxInAntiDiag(M, i, 0)) # start from left edge
        
        for i in range(len(M[0])):
            res = max(res, self.findMaxInCol(M, i))
            res = max(res, self.findMaxInDiag(M, 0, i))
            res = max(res, self.findMaxInAntiDiag(M, len(M)-1, i))
            
        
        return res
                
    def findMaxInRow(self, M, row):
        count, longest = 0, 0
        for n in M[row]:
            if n == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        return longest
    
    def findMaxInCol(self, M, col):
        count, longest = 0, 0
        for i in range(len(M)):
            if M[i][col] == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        return longest   
    
    def findMaxInDiag(self, M, row, col):
        count, longest = 0, 0
        while row < len(M) and col < len(M[0]):
            if M[row][col] == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
            row += 1
            col += 1
        return longest
    
    def findMaxInAntiDiag(self, M, row, col):
        count, longest = 0, 0
        while row >= 0 and col < len(M[0]):
            if M[row][col] == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
            row -= 1
            col += 1
        return longest
            
