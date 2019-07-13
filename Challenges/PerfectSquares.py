"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

"""
Time: O(n^2)
Space: O(n)
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_list = [1]
        
        s = 2  
        
        # Get all the possible square numbers upto n
        while s*s<=n:
            square_list.append(s*s)
            s+=1
            
        # init dp matrix for all the numbers in the range
        dp = [i for i in range(n+1)]
        
        # start from 1, go through all the numbers
        for i in range(1,n+1):
            # if the number is a square number, set the count for that number to 1
            if i in square_list:
                dp[i] = 1
            else:
                # otherwise, for the first number in the square list that is larger than or equal to the current number, 
                for j in square_list:
                    if j<= i:
                        # take min of current dp or the smaller square number added by the pervious number
                        dp[i] = min(dp[i],dp[j]+dp[i-j])
                    else:
                        break
        return dp[n]

_dp = [0]
    def numSquares(self, n):
        dp = self._dp
        while len(dp) <= n:
            dp += min(dp[-i*i] for i in range(1, int(len(dp)**0.5+1))) + 1,
        return dp[n]


class Solution:
    def numSquares(self, n):

        dp = [float("inf") for i in range(n + 1)]
        dp[1] = 1
        perfect = [1]
        for i in range(2, n + 1):
            if not i ** 0.5 - int(i ** 0.5):
                dp[i] = 1
                perfect.append(i)
            else:
                for j in perfect:
                    dp[i] = min(dp[i], dp[i - j] + 1)
        return dp[-1]

