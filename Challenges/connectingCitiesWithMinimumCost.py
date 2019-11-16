"""
Connecting Cities With Minimum Cost

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.  (A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that connects those two cities together.  The cost is the sum of the connection costs used. If the task is impossible, return -1.

 

Example 1:



Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.
Example 2:



Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
 

Note:

1 <= N <= 10000
1 <= connections.length <= 10000
1 <= connections[i][0], connections[i][1] <= N
0 <= connections[i][2] <= 10^5
connections[i][0] != connections[i][1]
"""

"""
Prim's Algo

Starting from city 1, BFS search all next cities, pick up the one with minimal cost, remove this city and add its following cities to BFS searching list.
Every time one city removed, many added.
e.g.
City 1 leads to city 2,3, and 4, of which city "3" has the least cost, and city "3" leads to city 7, then, add cost of city 3, move the next BFS search to city 2,4,7
1 -> 2,3,4 -> 2,4,7

Time: O(Nlog(N))
Space: O(E)
"""
class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)

        for c1, c2, cost in connections:
            graph[c1].append((cost, c2))
            graph[c2].append((cost, c1))
        
        pq = [(0, 1)]
        visited = [False]*(N+1)
        visited[0] = True
        res = 0
        while pq:
            cost, city = heapq.heappop(pq)
            if visited[city]:
                continue
            visited[city] = True
            res += cost
            for neiCost, nei in graph[city]:
                heapq.heappush(pq, (neiCost, nei))
        
        return res if all(visited) else -1
        

