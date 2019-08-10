"""
Number of Islands 2

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
"""

"""
Union Find
Positions =>N
Find ~= O(1), with path compression, the runtime for find is O(log*n) Which is different from O(logn). The complete proof is online.
Union ~= O(1)
Total O(N)
"""
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        isIsland = [[False for _ in range(n)] for _ in range(m)]
        unf = UnionFind(m,n)
        dx = [0,1,-1,0]
        dy = [1,0,0,-1]
        answer = []
        
        for position in positions:
            
            oj = position[0]
            oi = position[1]
            if not isIsland[oj][oi]:
                isIsland[oj][oi] = True
                unf.size += 1
        
            for i in range(4):
                nj = oj + dy[i]
                ni = oi + dx[i]
                
                if nj < m and ni < n and nj > -1 and ni > -1 and isIsland[nj][ni]:
                    unf.union(oj*n+oi, nj*n + ni)
            answer.append(unf.size)
        return answer
        
class UnionFind:
    
    def __init__(self, m, n):
        self.size = 0
        self.father = [0] * (m*n)
        for j in range(m):
            for i in range(n):
                self.father[j*n+i] = j*n + i
        
    def union(self, a, b):
        fa = self.find(a)
        fb = self.find(b)
        if fa != fb:
            self.father[fb] = fa
            self.size -= 1
        
    def find(self, child):
        
        j = child
        while j != self.father[j]:
            j = self.father[j]
            
        while child != self.father[child]:
            temp = self.father[child]
            self.father[child] = j
            child = temp
        return j

