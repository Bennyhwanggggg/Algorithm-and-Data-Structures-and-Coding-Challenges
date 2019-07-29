"""
Give a gird, and there are X and Y in this grid. find the shortest distance between X and Y.

Example 1:

Input:
[[X,0,0],
 [0,Y,0],
 [X,Y,0]] 
Output: 1
Example 2:

Input:
[[X,X,0],
 [0,0,Y],
 [Y,0,0]] 
Output: 2
"""

import collections

"""
BFS
Time: O(n*m)
Space: O(n*m)
"""
def findClosest(grid):
	m, n = len(grid), len(grid[0])
	directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
	queue = collections.deque()
	visited = set()

	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'X':
				queue.append(((i, j), 0))
				visited.add((i, j))

	while queue:
		for _ in range(len(queue)):
			(r, c), dist = queue.popleft()
			if grid[r][c] == 'Y':
				return dist
			for x, y in directions:
				new_r, new_c = r+x, c+y
				if new_r < 0 or new_c < 0 or new_r >= m or new_c >= n or (new_r, new_c) in visited:
					continue
				queue.append(((new_r, new_c), dist+1))
				visited.add((new_r, new_c))

	return -1

if __name__ == '__main__':
	grid = [['X', '0', '0'], 
        	['X', '0', '0'], 
        	['0', 'Y', 'Y']]
	assert findClosest(grid) == 2

	grid = [['X', 'X', '0'], 
        	['0', '0', 'Y'], 
        	['Y', '0', '0']]
	assert findClosest(grid) == 2

	grid = [['X', '0', '0'], 
        	['0', 'Y', '0'], 
        	['X', 'Y', '0']]
	assert findClosest(grid) == 1

