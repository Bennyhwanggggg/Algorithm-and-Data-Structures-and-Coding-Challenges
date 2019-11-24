"""
Number of Submatrices That Sum to Target

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

 

Example 1:

Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
 

Note:

1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8

"""

"""
1. calculate prefix sum for each row
for (int i = 0; i < m; i++)
    for (int j = 1; j < n; j++)
        A[i][j] += A[i][j - 1];
For this double-for loop, we are calculating the prefix sum for each row in the matrix, which will be used later

2. for every possible range between two columns, accumulate the prefix sum of submatrices that can be formed between these two columns by adding up the sum of values between these two columns for every row
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        int cur = 0;
        for (int k = 0; k < m; k++) {
            cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
            res += counter.getOrDefault(cur - target, 0);
            counter.put(cur, counter.getOrDefault(cur, 0) + 1);
        }
    }
}
To understand what this triple-for loop does, let us try an example, assume i = 1 and j = 3, then for this part of code:

Map<Integer, Integer> counter = new HashMap<>();
counter.put(0, 1);
int cur = 0;
for (int k = 0; k < m; k++) {
    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
    res += counter.getOrDefault(cur - target, 0);
    counter.put(cur, counter.getOrDefault(cur, 0) + 1);
}
I will break this piece of code into two major part:

Map<Integer, Integer> counter = new HashMap<>();
counter.put(0, 1);
key of this hashmap present the unique value of all possible prefix sum that we've seen so far
value of this hashmap represents the count (number of appearances) of each prefix sum value we've seen so far
an empty submatrix trivially has a sum of 0
for (int k = 0; k < m; k++) {
    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
    res += counter.getOrDefault(cur - target, 0);
    counter.put(cur, counter.getOrDefault(cur, 0) + 1);
}
Here we are actually calculating the prefix sum of submatrices which has column 1, 2, and 3, by adding up the sum of matrix[0][1...3], matrix[1][1...3] ... matrix[m-1][1...3] row by row, starting from the first row (row 0). The way of getting the number of submatrices whose sum equals to K uses the same idea of 560. Subarray Sum Equals K so I won't repeat it again.
"""
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        m, n = len(A), len(A[0])
        for row in A:
            for i in range(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.Counter({0: 1})
                cur = 0
                for k in range(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res

