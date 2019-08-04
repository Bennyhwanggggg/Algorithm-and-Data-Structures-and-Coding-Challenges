"""
Maximum Length of Repeated Subarray

Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

Example 1:

Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation: 
The repeated subarray with maximum length is [3, 2, 1].
 
Note:

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""

"""
DP

Intuition and Algorithm

Since a common subarray of A and B must start at some A[i] and B[j], let dp[i][j] be the longest common prefix of A[i:] and B[j:]. Whenever A[i] == B[j], we know dp[i][j] = dp[i+1][j+1] + 1. Also, the answer is max(dp[i][j]) over all i, j.

We can perform bottom-up dynamic programming to find the answer based on this recurrence. Our loop invariant is that the answer is already calculated correctly and stored in dp for any larger i, j.
Time: O(MN)
Space: O(MN)
"""
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0]*(len(B)+1) for _ in range(len(A)+1)]
        for i in range(len(A)-1, -1, -1):
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1]+1
        return max(max(row) for row in dp)

