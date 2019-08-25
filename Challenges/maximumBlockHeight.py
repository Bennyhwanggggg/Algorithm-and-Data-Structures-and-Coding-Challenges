"""
Given the left view and front view of the skyline of a block as two arrays, find the maximum total height of buildings in the block.

Example 1:

Input: leftView = [4, 2, 3], frontView = [3, 2, 3, 4]
Output: 31
Explanation: Based on the left and front view, the volume we'd be able to build on the block could be

[3, 2, 3, 4]    [3, 2, 3, 4]

[2, 2, 2, 2] or [2, 2, 2, 1]

[3, 2, 3, 3]    [1, 2, 3, 3]

The total height of buildings in the first matrix is the largest possible.
Therefore the maximum total height for the left and front views given is sum of the first matrix 31.
Example 2:

Input: leftView = [3, 5], frontView = [2, 5]
Output: 12
Explanation: Because the largest block volume to build is

[2, 3]
[2, 5]

Return sum 2 + 3 + 2 + 5 = 12.
"""

def maximumBlockHeight(leftView, frontView):
	res = 0
	for left in leftView:
		for front in frontView:
			res += min(left, front)
	return res

if __name__ == '__main__':
	assert maximumBlockHeight([4, 2, 3], [3, 2, 3, 4]) == 31
	assert maximumBlockHeight([3, 5], [2, 5]) == 12