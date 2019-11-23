"""
Predict the Winner

Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score.

Example 1:
Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return False.
Example 2:
Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.
Note:
1 <= length of the array <= 20.
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.
"""

"""
DP

The goal here is that we want to maximize the amount of money we can get assuming we move first.

Here your dp[i][j] means the max value we can get if it it's our turn and only coins between i and j remain.(Inclusively)

So dp[i][i] means there is only one coin left, we just pick it, dp[i][i+1] means there are only two left, we then pick the max one.

Now we want to derive the more general case. dp[i][j] = max( something + v[i], something + v[j]), since we either will pick the i or j coin. The problem now turns to what "something" here will be.

A quick idea may bedp[i][j] = max( dp[i + 1][j] + v[i], dp[i][j - 1] + v[j]), but here dp[i + 1][j] and dp[i][j - 1] are not the values directly available for us, it depends on the move that our opponent make.

Then we assume our opponent is as good as we are and always make optimize move. The worse case is that we will get the minimal value out of all possible situation after our opponent make its move.

so the correct dp formula would be dp[i][j] = max( min (dp[i + 1][j - 1], dp[i + 2][ j]) + v[i], min (dp[i][j - 2], dp[i + 1][ j - 1]) + v[j]}) .
If we pick i, then our opponent need to deal with subproblem dp[i + 1][j], it either pick from i + 2 or j - 1. Similarly, If we pick j, then our opponent need to deal with subproblem dp[i][j - 1] , it either pick from i + 1 or j - 2. We take the worse case into consideration so use min() here.
"""

"""
DP
Time: O(N^2)
Space: O(N^2)
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        dp = [[-1 for _ in range(len(nums))] for _ in range(len(nums))]
        
        def helper(v, dp, i, j):
            if i > j:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            a = v[i] + min(helper(v, dp, i+1, j-1), helper(v, dp, i+2, j))
            b = v[j] + min(helper(v, dp, i, j-2), helper(v, dp, i+1, j-1))
            dp[i][j] = max(a, b)
            return dp[i][j]
        
        res = helper(nums, dp, 0, len(nums)-1)
        return 2*res >= sum(nums)

"""
DP
Time: O(N^2)
Space: O(N)
"""
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        dp = [0]*len(nums)
        
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)):
                dp[j] = max(nums[i]-dp[j], nums[j]-dp[j-1])
        
        return dp[-1] >= 0

