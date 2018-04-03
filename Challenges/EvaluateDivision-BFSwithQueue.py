class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """

        graph = {}

        def buildGraph(equations, values):
            def add_edge(src, dest, val):
                if src in graph:
                    graph[src].append((dest, val))
                else:
                    graph[src] = [(dest, val)]

            for eq, val in zip(equations, values):
                src, dest = eq
                add_edge(src, dest, val)
                add_edge(dest, src, 1 / val)

        def findPath(query):
            num, den = query

            if num not in graph or den not in graph:
                return -1.0

            queue = collections.deque([(num, 1.0)])

            visited = set()

            while queue:
                num, product = queue.popleft()
                if num == den:
                    return product
                visited.add(num)
                for node, val in graph[num]:
                    if node not in visited:
                        queue.append((node, val * product))
            return -1.0

        buildGraph(equations, values)
        return [findPath(p) for p in queries]