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


