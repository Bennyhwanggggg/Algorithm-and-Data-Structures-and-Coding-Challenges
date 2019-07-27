"""
Array Permutation

Given 2 input arrays, one as the original and one that has been permuted. Use the reordering of the input array to reorder another array and return its result.

Example:

Input: a = [1, 2, 3, 4, 5], b = [4, 1, 2, 5, 3], c = [6, 7, 8, 9, 10]
Output: [9, 6, 7, 10, 8]
"""

"""
Time: O(N^2)
Space: O(N)
"""
def arrayPermutation(a, b, c):
	mapping = dict()
	# to avoid this, first store each element and their index in a map and do a second scan
	for idx, n in enumerate(a):
		mapping[idx] = b.index(n)

	res = [-1]*len(c)
	for idx, n in enumerate(c):
		res[mapping[idx]] = n

	return res

"""
Time: O(N)
Space: O(1)
Inplace
"""
def arrayPermutation(a, b, c):
	mapping = dict()
	# to avoid this, first store each element and their index in a map and do a second scan
	for idx, n in enumerate(a):
		mapping[idx] = b.index(n)

	res = [-1]*len(c)
	for idx, n in enumerate(c):
		res[mapping[idx]] = n

	return res

if __name__ == '__main__':
	assert arrayPermutation(a=[1, 2, 3, 4, 5], b =[4, 1, 2, 5, 3], c=[6, 7, 8, 9, 10]) == [9, 6, 7, 10, 8]