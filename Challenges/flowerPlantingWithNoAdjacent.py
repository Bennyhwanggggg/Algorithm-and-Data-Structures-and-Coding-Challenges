"""
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

 

Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Note:

1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.

"""


"""
DFS
Time: O(n)

The question points to this connection of gardens being a graph, so we create a graph with a dictionary. For each garden, we have a list of gardens it is connected to. Since this is bidirectional, we append to both gardens in each path.

How to chose order of which garden to plant flowers in first: I had trouble with this during the competition, until I reread the problem. It says that there are 4 flowers to choose from, but each garden can only have 3 edges. This means that there must be a flower to choose from for each garden and you don't have to worry about choosing the order of the garden to plant flowers in. If there are more than 3 edges connected to a garden, I think you'd have to sort the order of which gardens to plant flowers in by the number of edges it is connected to: #sortedEdges = sorted(((len(g[x]), x) for x in g), reverse = True).

We create a plantdict so we know which flower we're planting in each garden. We go through all the gardens and plant a flower. Everytime we plant a flower, we update our plantdict so that gardens that are connected will not plant the same flower.

For our answer, if the garden is not connected to any other node, we plant flower 1 just for simplicity. For example, one of the test cases is "10,000 []", which means there are 10,000 nodes with no connections, so we return [1]*N.

Runtime (I think): O(V + E) Space: O(V + E)
"""
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [None] * (N + 1)
        paths = map(sorted, paths) # space optimization, use directed graph, neighbor_index < cur_index
        graph = collections.defaultdict(list)
        for neighbor, cur in paths:
            graph[cur].append(neighbor)
        
        # dfs painting, check colors used by connected neighbor nodes
        def dfs(cur):
            used_colors = set([res[neighbor] for neighbor in graph[cur]])
            for color in range(1, 5):
                if color not in used_colors:
                    res[cur] = color
                    break
					
		# space optimization, call dfs() from low to high node index
        for cur in range(1, N + 1):
            dfs(cur)

        return res[1:]
    

class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        
        res = [0] * N
        #building graph from list of edges 
        G = [[] for i in range(N)]
        for x, y in paths:                   
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)   
        for i in range(N):
            used_colors = []
            for neighbor in G[i]:
                used_colors.append(res[neighbor]) #checking if seen or not seen, if seen, what is color? because its other neighbor will have other color
            for color in range(1, 5):
                if color not in used_colors:
                    res[i] = color
        return res

