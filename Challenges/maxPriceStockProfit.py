# Find the lowest point and the maximum point that occurs after it

# set current min and current max for the first point
# for each point compare it to currrent min max ans reset if need to
# compute difference and keep track of diff
#

def get_max_profit(prices):
	min_val = max_val = prices[0]
	diff = prices[1] - prices[0]

	for p in prices[1:]:
		diff = max(p-min_val, diff)
		min_val = min(p, min_val)
		max_val = max(p, max_val)
		

	return diff

prices = [10, 7, 5, 4, 3, 2]
print(get_max_profit(prices))



def get_max_profit2(stock_prices_yesterday):
	if len(stock_prices_yesterday) < 2:
		return
	min_price = stock_prices_yesterday[0]
	max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
	for p in stock_prices_yesterday[1:]:
		max_profit = max(p - min_price, max_profit)
		min_price = min(min_price, p)
	return max_profit


prices = [10, 7, 5, 4, 3, 2]
print(get_max_profit2(prices))