"""
You are given a list of non-negative integers. Find the largest value of the expression you can get by using +, * and ( ) operators.

Example:

Input: [1, 2, 1, 2]
Output: 9
Explanation: (1 + 2) * (1 + 2) = 9
Follow-up:
Negative values are allowed. -> in this case need to store max and min separetely
max[i][j] = max(max[i][k] + max[k][j], max[i][k] * max[k][j], min[i][k] * min[k][j]) for k in range(i, j)
"""


# dp L[i, j] = max([L[i, k] + L[k, j]] for k in range(i, j + 1) + [L[i, k] * L[k, j]] for k in range(i, j + 1))
def largestValue(nums):

	if len(nums) == 0:
		return 0

	dp = dict()

	def helper(nums, l, r):
		if l == r:
			return nums[l]

		if (l, r) in dp:
			return dp[(l, r)]

		res = 0
		for i in range(r-l):
			res = max(res, helper(nums, l, l+i) + helper(nums, l+i+1, r))
			res = max(res, helper(nums, l, l+i) * helper(nums, l+i+1, r))
		dp[(l, r)] = res
		return res

	helper(nums, 0, len(nums)-1)
	return dp[(0, len(nums)-1)]

if __name__ == '__main__':
	assert largestValue([1, 2, 1, 2]) == 9
	assert largestValue([1, 1, 1, 1, 2, 1, 10]) == 120