"""
Given an int array nums of length n. Split it into strictly decreasing subsequences. Output the min number of subsequences you can get by splitting.

Example 1:

Input: [5, 2, 4, 3, 1, 6]
Output: 3
Explanation:
You can split this array into: [5, 2, 1], [4, 3], [6]. And there are 3 subsequences you get.
Or you can split it into [5, 4, 3], [2, 1], [6]. Also 3 subsequences.
But [5, 4, 3, 2, 1], [6] is not legal because [5, 4, 3, 2, 1] is not a subsuquence of the original array.
Example 2:

Input: [2, 9, 12, 13, 4, 7, 6, 5, 10]
Output: 4
Explanation: [2], [9, 4], [12, 10], [13, 7, 6, 5]
Example 3:

Input: [1, 1, 1]
Output: 3
Explanation: Because of the strictly descending order you have to split it into 3 subsequences: [1], [1], [1]

"""

"""
Heapq
Time: O(n^2log(n)) because for each idx, we end up popping everything out in worst case
Space: O(N)
"""
import heapq

def decreasingSubsequence(nums):
	pq = []
	for idx, num in enumerate(nums):
		heapq.heappush(pq, (-num, idx))

	count = 0
	while pq:
		val, idx = heapq.heappop(pq)
		temp = []
		while pq:
			next_val, next_idx = heapq.heappop(pq)
			if next_idx < idx or -val <= -next_val:
				temp.append((next_val, next_idx))
			else:
				val = next_val
				idx = next_idx
		count +=1
		for remain in temp:
			heapq.heappush(pq, remain)
	return count


def decreasingSubsequence(nums):
	if not nums:
		return 0
	dp = [0] * len(nums)
	dp[-1] = 1
	ans = 1
	for i in range(len(dp)-1, -1, -1):
		length = 0
		curr = nums[i]
		for j in range(i+1, len(dp)):
			if nums[j] >= curr:
				length = max(length ,dp[j])
				curr = nums[j]
		dp[i] = length + 1
		ans = max(ans, dp[i])
	return ans


if __name__ == '__main__':
	assert decreasingSubsequence([5, 2, 4, 3, 1, 6]) == 3
	assert decreasingSubsequence([2, 9, 12, 13, 4, 7, 6, 5, 10]) == 4
	assert decreasingSubsequence([1, 1, 1]) == 3




