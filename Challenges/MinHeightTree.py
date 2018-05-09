import collections
class Solution:
    def findMinHeightTrees(self, n, edges):
        if not edges:
            if n == 1:
                return [0]
            else:
                return []
        table, wlist = [set() for i in range(n)], collections.deque()
        for e in edges:
            table[e[0]].add(e[1])
            table[e[1]].add(e[0])
        for i in range(n):
            if len(table[i]) == 1:
                wlist.append(i)
        steps = 0
        node1, node2 = n,n
        while(wlist):
            steps += 1
            len_level = len(wlist)
            if len_level == 1:
                return list(wlist)
            for i in range(len_level):
                prev_node1 = node1
                node1 = wlist.popleft()
                if node1 == node2:
                    return [node1,prev_node1]
                node2 = table[node1].pop()
                table[node2].remove(node1)
                if (len(table[node2]) == 1):
                    wlist.append(node2)
        return  list(wlist)


class Solution:
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1: return [0]
        graph = [set() for i in range(n)]
        for edge in edges:
            graph[edge[0]].add(edge[1])
            graph[edge[1]].add(edge[0])
        leaves = []
        for i in range(n):
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            temp_leaves = []
            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1: temp_leaves.append(j)
            leaves = temp_leaves
        return leaves