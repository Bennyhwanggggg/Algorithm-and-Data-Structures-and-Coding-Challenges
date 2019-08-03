"""
Number of Connected Components In An Undirected Graph

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to find the number of connected components in an undirected graph.

Example 1:

Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2:

Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.
"""

"""
BFS
Time: O(V+E)
Space: O(V+E)
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()
        ans = 0
        for node in range(n):
            if node in visited:
                continue
            
            queue = collections.deque([node])
            while queue:
                curr = queue.popleft()
                visited.add(curr)
                for nei in graph[curr]:
                    if nei not in visited:
                        queue.append(nei)
                
            ans += 1
        
        return ans
            


class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        def dfs(graph, used, start):
            used.add(start)
            for dest in graph[start]:
                if dest not in used:
                    used = dfs(graph, used, dest)
            return used

        graph = {}

        for v, w in edges:
            if v not in graph:
                graph[v] = []
            graph[v].append(w)
            if w not in graph:
                graph[w] = []
            graph[w].append(v)
        for n in range(n):
            if n not in graph:
                graph[n] = []

        count = 0
        used = set()
        for source, dests in graph.items():
            if source not in used:
                used = dfs(graph, used, source)
                count += 1
        return count


