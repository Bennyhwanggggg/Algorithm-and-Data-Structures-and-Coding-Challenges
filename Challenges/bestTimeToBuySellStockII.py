"""
Best Time to Buy And Sell Stock II

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
"""

"""
Peak Valley Approach
Time: O(n)
Space: O(1)
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        valley = prices[0]
        peak = prices[0]
        i = 0
        profit = 0
        while i < len(prices):
            while i < len(prices)-1 and prices[i] > prices[i+1]:
                i += 1
            valley = prices[i]
            while i < len(prices)-1 and prices[i] < prices[i+1]:
                i += 1
            peak = prices[i]
            profit += peak-valley
            i += 1
        return profit

