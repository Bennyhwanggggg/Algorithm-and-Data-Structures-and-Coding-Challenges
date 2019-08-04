"""
Minimum Height Tree

For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
Note:

According to the definition of tree on Wikipedia: “a tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.”
The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

"""

"""
Here is one insight for this problem: the root of MHT is the middle point of the longest path in the tree; hence there are at most two MHT roots.

How to find them? We can BFS from the bottom (leaves) to the top until the last level with <=2 nodes. To build the current level from the previous level, we can monitor the degree of each node. If the node has degree of one, it will be added to the current level. Since it only check the edges once, the complexity is O(n).
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1: 
            return [0]
        neighbors = collections.defaultdict(list)
        degrees = collections.defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degrees[u] += 1
            degrees[v] += 1

        # First find the leaves
        preLevel, unvisited = [], set(range(n))
        for i in range(n):
            if degrees[i] == 1: 
                preLevel.append(i)

        while len(unvisited) > 2:
            thisLevel = []
            for u in preLevel:
                unvisited.remove(u)
                for v in neighbors[u]:
                    if v in unvisited: 
                        degrees[v] -= 1
                        if degrees[v] == 1: 
                            thisLevel.append(v)
            preLevel = thisLevel

        return preLevel


"""
Longest Path

It is easy to see that the root of an MHT has to be the middle point (or two middle points) of the longest path of the tree.
Though multiple longest paths can appear in an unrooted tree, they must share the same middle point(s).

Computing the longest path of a unrooted tree can be done, in O(n) time, by tree dp, or simply 2 tree traversals (dfs or bfs).
The following is some thought of the latter.

Randomly select a node x as the root, do a dfs/bfs to find the node y that has the longest distance from x.
Then y must be one of the endpoints on some longest path.
Let y the new root, and do another dfs/bfs. Find the node z that has the longest distance from y.

Time: O(N)
Space: O(N)
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = collections.defaultdict(set)
        for v, w in edges:
            neighbors[v].add(w)
            neighbors[w].add(v)
            
        def maxpath(v, visited):
            visited.add(v)
            paths = [maxpath(w, visited) for w in neighbors[v] if w not in visited]
            path = max(paths or [[]], key=len)
            path.append(v)
            return path
        
        path = maxpath(0, set())
        path = maxpath(path[0], set())
        m = len(path)
        return path[(m-1)//2:m//2+1]


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
