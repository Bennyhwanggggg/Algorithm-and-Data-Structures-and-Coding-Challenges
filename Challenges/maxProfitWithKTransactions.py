

def maxProfitWithKTransactions(prices, k):
    if not len(prices):
		return 0
	dp = [[0 for _ in range(len(prices))] for _ in range(k+1)]
	for t in range(1, k+1):
		maxThusFar = -float('inf')
		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, dp[t-1][d-1] - prices[d-1])
			dp[t][d] = max(dp[t][d-1], maxThusFar + prices[d])
	return dp[-1][-1]

