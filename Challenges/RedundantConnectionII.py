class Solution:
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        nodes = set()
        parent = collections.defaultdict(list)
        for node, child in edges:
            nodes.add(node)
            nodes.add(child)
            parent[child].append(node)

        if nodes - set(parent.keys()):
            for child, parents in parent.items():
                if len(parents) == 2:
                    break
            res = [parents[1], child]
            for p in parents:
                node = p
                while parent[node] and node != child:
                    node = parent[node][0]
                if node == child:
                    res = [p, child]

            return res
        else:
            seen = []
            while node not in seen:
                seen.append(node)
                node = parent[node][0]

            cycle = set(seen[seen.index(node):])
            for a, b in reversed(edges):
                if a in cycle and b in cycle:
                    return [a, b]

