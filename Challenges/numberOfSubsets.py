"""
For a given list of integers and integer K, find the number of non-empty subsets S such that min(S) + max(S) <= K.

Example 1:

nums = [2, 4, 5, 7]
k = 8
Output: 5
Explanation: [2], [4], [2, 4], [2, 4, 5], [2, 5]
Example 2:

nums = [1, 4, 3, 2]
k = 8
Output: 15
Explanation: 16 (2^4) - 1 (empty set) = 15
Example 3:

nums = [2, 4, 2, 5, 7]
k = 10
Output: 27
Explanation: 31 (2^5 - 1) - 4 ([7], [5, 7], [4, 5, 7], [4, 7]) = 27
Expected O(n^2) time solution or better.
"""


# Sliding Window O(nlog(n))
def countSubsets(nums, k):
	nums.sort()
	count = 0
	low, high = 0, len(nums)-1
	while low <= high:
		if nums[low] + nums[high] > k:
			high -= 1
		else:
			count += 2 ** (high - low)
			low += 1
	return count

if __name__ == '__main__':
	assert countSubsets([2, 4, 5, 7], 8) == 5
	assert countSubsets([1, 4, 3, 2], 8) == 15
	assert countSubsets([2, 4, 2, 5, 7], 10) ==27


