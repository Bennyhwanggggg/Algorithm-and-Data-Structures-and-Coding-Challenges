"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Solution:
Use DP to solve this problem. It is obviously to come up with DP, because this is a "stage-decision-problem", every day we decide buy/sell/rest.

The state is defined as below

dp(n, 0) -> The max profix we get on day n, if we rest on day n.
dp(n, 1) -> The max profix we get on day n, if we buy on day n.
dp(n, 2) -> The max profix we get on day n, if we sell on day n.
Below is the state transition function

dp(n, 0) = max{ dp(n-1, 1), dp(n-1, 0), dp(n-1, 2) }, if we rest on day n, we do not really care about what we have done on day n-1, 
you can do whatever you want, and we just take the max profit from day n-1
dp(n, 1) = dp[n-1][0] - prices[n], if we buy on day n, we cannot buy on day n-1, because double-buy is by natural disallowed in the "Stock" Series.
We cannot sell on day n-1, because of the new cool-down policy. So in day n-1, we can only rest.
dp(n, 2) = max {dp(0, 1), dp(1, 1), ...., dp(n-1, 1)} + prices[n], if we sell on day n, we need to make sure we buy the stock before in one of (0...n-1).
For example, if you rest on the first 2 days, there is NOTHING for you to sell on the 3rd day. Among all the possible "buy-day", we pick the one with max-profix

Now, you might think: hmmmm, this is an O(N^2) DP because of 3., we need to get max from a list of values in each iteration. Not really, 
you can keep track of the max of the past dp(n, 1). In the following solution, I use the var bought to keep track.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = float('-inf')
        bought = dp[0][1]
        
        n = len(prices)
        for i in range(1, n):
            dp[i][0] = max([dp[i-1][0], dp[i-1][2], dp[i-1][1]])
            dp[i][1] = dp[i-1][0] - prices[i]
            dp[i][2] = bought + prices[i]            
            bought = max(bought, dp[i][1])
            
        return max(dp[n-1])


"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
"""

"""
DP，we can create two array, buy and sell. buy[i] means we buy a stock at day i , and sell[i] means we sell a stock at day i.

so, we have two equations :

buy[i] = max(buy[i-1] , sell[i-2] - prices[i]) // So we should use sell[i-2] means we cooldown one day.
sell[i] = max(sell[i-1],buy[i-1] + prices[i])
finally, return the max(buy[n-1] , sell[n-1]) （it is obvious that sell[n-1] >= buy[n-1] ,so we return sell[n-1]）

Time: O(n)
Space: O(n)   You can do it in O(1) space, since i rely on only i-1 and i-2, but I think you know it
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        n = len(prices)
        buy, sell = [0]*n, [0]*n
        buy[0] = -prices[0]
        buy[1] = -min(prices[0], prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        for i in range(2, n):
            buy[i] = max(sell[i-2] - prices[i], buy[i-1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
        return sell[n-1]     


"""
The natural states for this problem is the 3 possible transactions : buy, sell, rest. Here rest means no transaction on that day (aka cooldown).

Then the transaction sequences can end with any of these three states.

For each of them we make an array, buy[n], sell[n] and rest[n].

buy[i] means before day i what is the maxProfit for any sequence end with buy.

sell[i] means before day i what is the maxProfit for any sequence end with sell.

rest[i] means before day i what is the maxProfit for any sequence end with rest.

Then we want to deduce the transition functions for buy sell and rest. By definition we have:

buy[i]  = max(rest[i-1]-price, buy[i-1]) 
sell[i] = max(buy[i-1]+price, sell[i-1])
rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
Where price is the price of day i. All of these are very straightforward. They simply represents :

(1) We have to `rest` before we `buy` and 
(2) we have to `buy` before we `sell`
One tricky point is how do you make sure you sell before you buy, since from the equations it seems that [buy, rest, buy] is entirely possible.

Well, the answer lies within the fact that buy[i] <= rest[i] which means rest[i] = max(sell[i-1], rest[i-1]). That made sure [buy, rest, buy] is never occurred.

A further observation is that and rest[i] <= sell[i] is also true therefore

rest[i] = sell[i-1]
Substitute this in to buy[i] we now have 2 functions instead of 3:

buy[i] = max(sell[i-2]-price, buy[i-1])
sell[i] = max(buy[i-1]+price, sell[i-1])
This is better than 3, but

we can do even better

Since states of day i relies only on i-1 and i-2 we can reduce the O(n) space to O(1).


Time: O(N)
Space: O(1)
"""   
def maxProfit(self, prices):
    if len(prices) < 2:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell
