"""
One and Zeroes


In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
 

Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”
 

Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""

"""
DP

This question is very similar to a 0-1 knapsack, the transition function is

dp(k, x, y) = max(dp(k-1, x-z, y-o) + 1, dp(k-1, x, y))   (z is zeroes in strs[k], o is ones in strs[k])
dp(k, x, y) is the maximum strs we can include when we have x zeros, y ones and only the first k strs are considered.

dp(len(strs), M, N) is the answer we are looking for


This problem can be solved by using 2-D Dynamic Programming. We can make use of a dp array, such that an entry dp[i][j]denotes the maximum number of strings that can be included in the subset given only i 0's and j 1's are available.

Now, let's look at the process by which we'll fill the dpdp array. We traverse the given list of strings one by one. Suppose, at some point, we pick up any string s_ks consisting of x zeroes and y ones. Now, choosing to put this string in any of the subset possible by using the previous strings traversed so far will impact the element denoted by dp[i][j] for i and j satisfying x ≤ i ≤ m, y ≤ j ≤ n. This is because for entries dp[i][j] with i < xi<x or j < yj<y, there won't be sufficient number of 1's and 0's available to accomodate the current string in any subset.

Thus, for every string encountered, we need to appropriately update the dpdp entries within the correct range.

Further, while updating the dpdp values, if we consider choosing the current string to be a part of the subset, the updated result will depend on whether it is profitable to include the current string in any subset or not. If included in the subset, the dp[i][j] entry needs to be updated as dp[i][j]=1+dp[i−zeroes_current_string][j−ones_current_string], where the factor of +1 takes into account the number of elements in the current subset being increased due to a new entry.

But, it could be possible that the current string could be so long that it could be profitable not to include it in any of the subsets. Thus, the correct equation for dpdp updation becomes:

dp[i][j]=max(1+dp[i−zeroes_current_string][j−ones_current_string],dp[i][j])

Thus, after the complete list of strings has been traversed, dp[m][n] gives the required size of the largest subset.

=========

Find the maximum strings which can be created using m zeroes and n ones using indices 0 to i in strs (strs[0:i+1]) and store the results in a three dimensional table. The answer to the problem is then table[m,n,i]
For simplicity, we will parameterize i as the number of strings being used in strs so that we dont need to deal with negative indices.
Iterate from index 1 to len(strs). For a given index, we test all possible pairs of m and n.
If for a pair we find we have sufficient zeroes and ones to use str[i], we update table[i,j,k] as the max of table[i-1,j, k], 1+table[i-1,j-zeroes,k-ones]. This means that we are trying to find the maximum by either including it or not including it. For the case of inclusion, we need to find the maximum string we can until index i-1 with j-zeroes and k-ones.
If for a pair we find we do not have sufficient zeroes and ones, we update table[i,j,k] as table[i-1,j,k].
"""
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        prev, curr = [[0]*(n+1) for _ in range(m+1)], [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, len(strs)+1):
            zeroes, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    curr[j][k] = 0
                    if j >= zeroes and k >= ones:
                        curr[j][k] = max(prev[j][k], 1+prev[j-zeroes][k-ones])
                    else:
                        curr[j][k] = prev[j][k]
            prev, curr = curr, prev
        return prev[m][n]
                

