"""
Best Time to Buy and Sell Stock IV

Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
"""

"""
Time: O(NK)
Space: O(N)
"""
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        
        if k >= n//2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i - j > 0)
        
        profits = [0]*n  # max profit up to jth transaction
        for j in range(k):  # for each many transaction, we compare it to see if it was possible to make a larger profit with a less transaction amount
            preprofit = 0  # The max profit with i transations and selling stock on day j.
            for i in range(1, n):
                profit = prices[i] - prices[i-1]  # profit we can make buy selling today
                preprofit = max(preprofit+profit, profits[i])  # get max if we include todays profit (include a new transaction)
                profits[i] = max(profits[i-1], preprofit)  # compare the profit to if we didnt make a transaction
    
        return profits[-1]

