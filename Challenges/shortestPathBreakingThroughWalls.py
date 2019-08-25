"""
Given a 2D grid of size r * c. 0 is walkable, and 1 is a wall. You can move up, down, left or right at a time. Now you are allowed to break at most 1 wall, what is the minimum steps to walk from the upper left corner (0, 0) to the lower right corner (r-1, c-1)?

Example 1:

Input:
[[0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [1, 1, 0, 1, 0],
 [1, 1, 1, 1, 0]]

Output: 7
Explanation: Change `1` at (0, 1) to `0`, the shortest path is as follows:
(0, 0) -> (0, 1) -> (0, 2) -> (0, 3) -> (0, 4) -> (1, 4) -> (2, 4) -> (3, 4)
There are other options of length 7, not listed here.
Example 2:

Input:
[[0, 1, 1],
 [1, 1, 0],
 [1, 1, 0]]

Output: -1
Explanation: Regardless of which `1` is changed to `0`, there is no viable path.
Follow-up:
What if you can break k walls?

Example 1:

Input: k = 2
[[0, 1, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 1, 1, 1, 1],
 [0, 1, 1, 1, 1],
 [1, 1, 1, 1, 0]]

Output: 10
Explanation: Change (2, 4) and (3, 4) to `0`.
Route (0, 0) -> (1, 0) -> (1, 1) -> (1, 2) -> (0, 2) -> (0, 3) -> (0, 4) -> (1, 4) -> (2, 4) -> (3, 4) -> (4, 4)
"""


"""
Python BFS => queue while keeping track of number of walls broken
Time: O(MN)
Space: O(MN)
"""
def shortest_path_break_through_k_walls(grid: List[List[int]], k: int) -> int:
    q, visited, level = collections.deque([(0, 0, 0)]), {(0, 0, 0)}, 0
    while q:
        level += 1
        for _ in range(len(q), 0, -1):
            r, c, walls_broken = q.popleft()
            if (r, c) == (len(grid) - 1, len(grid[0]) - 1): return level - 1
            for dr, dc in zip([1, -1, 0, 0], [0, 0, 1, -1]):
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                    _next = (nr, nc, walls_broken + grid[nr][nc])
                    if _next[2] <= k and _next not in visited:
                        q.append(_next)
                        visited |= {_next}
    return -1