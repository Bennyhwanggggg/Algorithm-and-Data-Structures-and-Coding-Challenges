"""
In a binary matrix (all elements are 0 and 1), every row is sorted in ascending order (0 to the left of 1). Find the leftmost column index with a 1 in it.

Example 1:

Input:
[[0, 0, 0, 1],
 [0, 0, 1, 1],
 [0, 1, 1, 1],
 [0, 0, 0, 0]]
Output: 1
Example 2:

Input:
[[0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0],
 [0, 0, 0, 0]]
Output: -1
Expected solution better than O(rows * cols).
"""

"""
Time complexity: O(rows + cols).
Space complexity: O(1).
"""
def leftMostColumnIndexOfOne(grid):
	m, n = len(grid), len(grid[0])

	row = 0
	col = n-1
	res = float('inf')
	while row < m and col >= 0:
		if grid[row][col] == 1:
			res = min(res, col)
			col -= 1
		else:
			row += 1
	return res if res != float('inf') else -1

if __name__ == '__main__':
	assert leftMostColumnIndexOfOne([[0, 0, 0, 1],
																 	 [0, 0, 1, 1],
																 	 [0, 1, 1, 1],
																 	 [0, 0, 0, 0]]) == 1

	assert leftMostColumnIndexOfOne([[0, 0, 0, 1],
																 	 [0, 0, 1, 1],
																 	 [0, 0, 1, 1],
																 	 [0, 0, 0, 0]]) == 2

	assert leftMostColumnIndexOfOne([[0, 0, 0, 0],
																 	 [0, 0, 1, 1],
																 	 [0, 0, 1, 1],
																 	 [0, 0, 0, 0]]) == 2

	assert leftMostColumnIndexOfOne([[0, 0, 0, 0],
																 	 [0, 0, 0, 0],
																 	 [0, 0, 0, 0],
																 	 [0, 0, 0, 0]]) == -1

