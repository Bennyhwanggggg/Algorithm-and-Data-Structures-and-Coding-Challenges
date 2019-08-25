"""
Lottery Game

Several coupons are placed in a row, and to win the prize you need to pick at least 2 coupons of the same value. You can only pick consecutive coupons from the row. Each coupon costs 1 coin, find the minimum number of coins needed to obtain the prize or, -1 if it's not possible.

Example 1:

Input: coupons = [5, 3, 4, 2, 3, 4, 5, 7]
Output: 4
Explanation:
Because you can buy coupons with values [3, 4, 2, 3] or [4, 2, 3, 4]
Example 2:

Input: coupons = [3, 6, 1, 9]
Output: -1
"""

"""
Hashmap
Time: O(N)
Space: O(N)
"""
def lotterGame(coupons):
	res = float('inf')
	seen = dict()
	for idx, n in enumerate(coupons):
		if n in seen:
			res = min(res, idx - seen[n] + 1)
		seen[n] = idx

	return res if res != float('inf') else -1

if __name__ == '__main__':
	assert lotterGame([5, 3, 4, 2, 3, 4, 5, 7]) == 4
	assert lotterGame([3, 6, 1, 9]) == -1