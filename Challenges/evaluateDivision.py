"""
Equations are given in the format A / B = k, where A and B are variables represented as strings, and k is a real number (floating point number). Given some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].
"""

"""
BFS using queue
Time:
Given the number of variables N, and number of equations E,
building the graph takes O(E), each query takes O(N), space for graph takes O(E)
"""
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        if not len(equations):
            return -1.0

        graph = collections.defaultdict(list)
        for equation, value in zip(equations, values):
            num, denom = equation
            graph[num].append((denom, value))
            graph[denom].append((num, 1/value))
            
        res = []
        for query in queries:
            ans = -1.0
            num, denom = query
            if not denom in graph or not num in graph:
                res.append(-1.0)
                continue
            queue = collections.deque([(num, 1.0)])
            visited = set()
            while queue:
                curr, currProduct = queue.popleft()
                if curr == denom:
                    ans = currProduct
                    break
                visited.add(curr)
                for neighbour, val in graph[curr]:
                    if neighbour not in visited:
                        queue.append((neighbour, val*currProduct))
            res.append(ans)
        
        return res
            
