# basically find number of islands
class Solution:
    def removeStones(self, stones):
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)
        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(list), collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island


"""
Most Stones removed with same row or column

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?
"""

"""
DFS
Time: O(N^2) since we need to build the graph
Space: O(N^2) from graph

Count the connected components in the graph.
"""
class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        
        # Graph building by finding all the stones up to the current index
        # that have common x or y
        grid = collections.defaultdict(list)
        for i, x in enumerate(stones):
            for j in range(i):
                y = stones[j]
                if x[0] == y[0] or x[1] == y[1]:
                    grid[i].append(j)
                    grid[j].append(i)
            
        # DFS
        N = len(stones)
        res = 0
        seen = [False] * N
        for i in range(N):
            if not seen[i]:
                stack = [i]
                seen[i] = True
                while stack:
                    res += 1 # increment result based on the number of component
                    node = stack.pop()
                    for n in grid[node]:
                        if not seen[n]:
                            stack.append(n)
                            seen[n] = True
                res -= 1 # remove a node for the case where a component is by itself
        return res

