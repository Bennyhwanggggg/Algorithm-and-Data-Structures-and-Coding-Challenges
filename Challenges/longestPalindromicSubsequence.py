"""
Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
"""

"""
every adjacent number pair contains exactly one even and one odd, j just changes between 0 and 1,
DP
Time: O(N^2)
Space: O(2N)
"""
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[1]*2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in (range(j-1, -1, -1)):
                if s[i] == s[j]:
                    dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
        return dp[0][(n-1)%2]
    
"""
DP
Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [1] * n
        for j in range(1, len(s)):
            pre = dp[j]
            for i in (range(j-1, -1, -1)):
                tmp = dp[i]
                if s[i] == s[j]:
                    dp[i] = 2 + pre if i + 1 <= j - 1 else 2
                else:
                    dp[i] = max(dp[i + 1], dp[i])
                pre = tmp
        return dp[0]
    
"""
What is really happening with DP solution is it follows a simple brute force approach, that it tries to find the longest palindrome substring w/ respect to the position of each character: For example: "BBBAB"
We want to know the longest Palindrome from:
BBBAB
BBAB
BAB
AB
B

But notice, if you're viewing this backwards, B contains information that AB can use, and AB contains information that BAB can use, and indeed, true to the nature of DP, we can make use of information from previous calculations.

The tricky part is representing this in a data structure for our memoization, and we'll go with an intial matrix to represent the example above:
__B B B A B
B 1
B 0 1
B 0 0 1
A 0 0 0 1
B 0 0 0 0 1

So what the heck is happening here? Why ones and zeros? If you look at the table, it's quite simple, If we're looking at our first B, from BBBAB, we obviously only have 1 palindrome so far, and that is "B" BBAB, and likewise, if we're looking at the first B on BBAB, then we have 1 so far as "B" BAB, and the B before BBAB, is set to zero because technically, true to our idea, if we're looking at BBAB, we shouldn't have any info about the B before BBAB.

From then on we simply build our table with the following logic, if the current row character matches the column character, then we take value from row+1 and column-1, and increment by 2. Why? Suppose we have BCCCB, if we're looking BCCCB vs CCCB, BCCCB has a length of 5 that is a paldinrome, while CCCB has 3 (CCC), so the difference is 2.

Also if you think about it, from the table's standpoint, row+1 and column-1 would represent CCC, since the current column char is B, while the next row's starting chair is "C" CC.

If it doesn't match, then we take the max between the left value, and the bottom value of our current position. Why? Consider this, if we have BBA, and BA, we know that BBA has a value of 2, while BA is 1, so if we're looking at another character, say BBA "C" from the point of view of "B" BAC, then we still have a value of 2, while "B" AC is still 1.

So if you fill the table, you'll eventually get the following:
__B B B A B
B 1 2 3 3 4
B 0 1 2 2 3
B 0 0 1 1 3
A 0 0 0 1 1
B 0 0 0 0 1

We are actually going to traverse the table diagonally since that's the only way to fill the table in a way that we can access information from the [row+1, column-1], [row+1, column], [row, column-1]
"""
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        Use DP
        """
        str_len = len(s)
        dp_matrix = [[0]*len(s) for i in range(str_len)]
        
        k = 0
        while k < str_len:
            for i in range(str_len-k):
                j = i + k
                if i == j:
                    dp_matrix[i][j] = 1
                elif s[i] == s[j]:
                    dp_matrix[i][j] = dp_matrix[i+1][j-1] + 2
                else:
                    dp_matrix[i][j] = max(dp_matrix[i][j-1], dp_matrix[i+1][j])
            k += 1
                 
        return dp_matrix[0][str_len-1]

