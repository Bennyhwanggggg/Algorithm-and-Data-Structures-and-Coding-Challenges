"""
Apply one permutation to another
"""

"""
O(N) time and O(1) space

There is a trivial O(n^2) algorithm, but you can do this in O(n). E.g.:

A = [a, b, c, d, e]

P = [4, 3, 2, 0, 1]

We can swap each element in A with the right element required by P, after each swap, there will be one more element in the right position, and do this in a circular fashion for each of the positions (swap elements pointed with ^s):

[a, b, c, d, e] <- P[0] = 4 != 0 (where a initially was), swap 0 (where a is) with 4
 ^           ^
[e, b, c, d, a] <- P[4] = 1 != 0 (where a initially was), swap 4 (where a is) with 1
    ^        ^
[e, a, c, d, b] <- P[1] = 3 != 0 (where a initially was), swap 1 (where a is) with 3
    ^     ^
[e, d, c, a, b] <- P[3] = 0 == 0 (where a initially was), finish step
After one circle, we find the next element in the array that does not stay in the right position, and do this again. So in the end you will get the result you want, and since each position is touched a constant time (for each position, at most one operation (swap) is performed), it is O(n) time.

Use index array to store corresponding info
"""
def applyPermutation(arr, index):
	for i in range(len(arr)):
		while index[i] != i:
			# store vales of the target or correct position before swapping
			oldTargetIdx = index[index[i]] 
			oldTargetEle = arr[index[i]]

			# place arr[i] at its target position and also copy the corrected index for the new pos
			arr[index[i]] = arr[i]
			index[index[i]] = index[i]

			# copy old target values to arr[i] and index[i]
			index[i] = oldTargetIdx 
			arr[i] = oldTargetEle 
	
	return arr

"""
Python Concise
"""
def applyPermutation2(arr, index):
	for i in range(len(arr)):
		while index[i] != i:
			arr[index[i]], arr[i] = arr[i], arr[index[i]]
			index[index[i]], index[i] = index[i], index[index[i]] 
	
	return arr

if __name__ == '__main__':
	assert applyPermutation(['a', 'b', 'c', 'd', 'e'], [4, 3, 2, 0, 1]) == ['d', 'e', 'c', 'b', 'a']
	assert applyPermutation(['a', 'b', 'c', 'd', 'e'], [4, 3, 2, 1, 0]) == ['e', 'd', 'c', 'b', 'a']
	assert applyPermutation2(['a', 'b', 'c', 'd', 'e'], [4, 3, 2, 0, 1]) == ['d', 'e', 'c', 'b', 'a']
	assert applyPermutation2(['a', 'b', 'c', 'd', 'e'], [4, 3, 2, 1, 0]) == ['e', 'd', 'c', 'b', 'a']
