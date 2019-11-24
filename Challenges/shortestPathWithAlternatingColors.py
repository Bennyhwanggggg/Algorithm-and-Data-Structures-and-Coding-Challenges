"""
Shortest Path with Alternating Colors

Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue, and there could be self-edges or parallel edges.

Each [i, j] in red_edges denotes a red directed edge from node i to node j.  Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.

Return an array answer of length n, where each answer[X] is the length of the shortest path from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).

 

Example 1:

Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
Output: [0,1,-1]
Example 3:

Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
Output: [0,-1,-1]
Example 4:

Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
Output: [0,1,2]
Example 5:

Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
Output: [0,1,1]
 

Constraints:

1 <= n <= 100
red_edges.length <= 400
blue_edges.length <= 400
red_edges[i].length == blue_edges[i].length == 2
0 <= red_edges[i][j], blue_edges[i][j] < n
"""

"""
BFS
Time: O(E)
Space: O(E)
"""

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        
        RED, BLUE = 1, 0
        
        queue = collections.deque()
        
        for i, j in red_edges:
            graph[i].append((j, RED))
            if i == 0:
                queue.append((j, 1, RED))
        
        for i, j in blue_edges:
            graph[i].append((j, BLUE))
            if i == 0:
                queue.append((j, 1, BLUE))
        
        visited = set()
        res = [-1]*n
        res[0] = 0
        
        while queue:
            node, dst, color = queue.popleft()
            visited.add((node, color))
            res[node] = min(res[node] ,dst) if res[node] != -1 else dst
            for nei, neiColor in graph[node]:
                if neiColor != color and (nei, neiColor) not in visited:
                    visited.add((nei, neiColor))
                    queue.append((nei, dst+1, neiColor))
        
        return res
