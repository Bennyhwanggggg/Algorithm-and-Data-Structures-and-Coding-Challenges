"""
Compare String
 
One string is strictly smaller than another when the frequency of occurrence of the smallest
character in the string is less than the frequency of the occurrence of the 
smallest character in the comparison string.

For example, string "abcd" is smaller than string "aaa" because the smallest
character in "abcd" is "a" with a frequency of 1, and the smallest character
in "aaa" is also "a", but with a frequency of 3. In another example, string "a"
is samller than string "bb" because the smallest character in "a" is "a" with a 
frequency of 1, and the smallest character in "bb" is "b" with a frequency of 2.

Write a function that given string A (which contains M strings delimited by ',')
and string B (which contains N strings delimited by ','), returns an array C of N
integers. For 0 <= J < N, values of C[j] specify the number of strings in A which
are strictly smaller than the comparision Jth string in B.
"""
import collections
import bisect

def binarySearch(arr, val):
	left, right = 0, len(arr)
	while left < right:
		mid = (left + right) // 2
		if arr[mid] >= val:
			right = mid
		else:
			left = mid + 1
	return left


def compareStrings(A, B):
	stringA = A.split(',')
	stringB = B.split(',')

	lowest_As = []
	for strA in stringA:
		counts = collections.Counter(strA)
		lowest_As.append(counts[sorted(counts.keys())[0]])
	lowest_As.sort()


	res = []
	for strB in stringB:
		counts = collections.Counter(strB)
		lowest_B = counts[sorted(counts.keys())[0]]
		res.append(binarySearch(lowest_As, lowest_B))  # or use bisect to find the left insertion index => res.append(bisect.bisect_left(lowest_As, lowest_B))

	print(res)
	return res

if __name__ == '__main__':
	assert compareStrings("abcd,aabc,bd", "aaa,aa") == [3, 2]


