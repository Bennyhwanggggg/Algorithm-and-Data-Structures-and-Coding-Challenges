"""
Time: O(n)
Space O(1)
"""

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        buy = prices[0]
        profit = 0
        for p in prices:
            buy = min(p, buy)
            profit = max(profit, p-buy)
        return profit
