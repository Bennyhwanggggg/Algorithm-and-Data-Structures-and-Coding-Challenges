"""
Network Delay Time

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:
N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
"""

"""
DFS
Time: O(N^N + Elog(E)), we only visit each node up to N-1 times, one per each other node. We also have to explore every edge and sort them.
Space: O(N+E)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        
        for u, v, w in times:
            graph[u].append((w, v))
            
        dist = {node: float('inf') for node in range(1, N+1)}
        
        def dfs(node, curr_dist):
            if curr_dist >= dist[node]:
                return
            dist[node] = curr_dist
            for time, nei in sorted(graph[node]):
                dfs(nei, curr_dist+time)
        
        dfs(K, 0)
        ans = max(dist.values())
        return ans if ans < float('inf') else -1
    
"""
Dijkstra using heap
Time: O(N^2 + E) where E is the length of time and O(E log E) is the heap as potentially every edge is added to the heap
Space: O(N+E), the size of the graph O(E) plus the size of the other objects used O(N)
"""
class Solution(object):
    def networkDelayTime(self, times, N, K):
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        pq = [(0, K)]
        dist = {}
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist: 
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d+d2, nei))

        return max(dist.values()) if len(dist) == N else -1


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        recieved = set()
        network = collections.defaultdict(list)
        for u, v, w in times:
            network[u].append((w, v))
        
        if K not in network.keys():
            return -1
        dist = dict()
        pq = [(0, K)]
        while pq:
            if len(dist.keys()) == N:
                break
            d, node = heapq.heappop(pq)
            if node in dist.keys():
                continue
            dist[node] = d
            for distance, neightbour in network[node]:
                if neightbour not in dist.keys():
                    heapq.heappush(pq, (distance+d, neightbour))
        return -1 if len(dist.keys()) != N else max(dist.values())
