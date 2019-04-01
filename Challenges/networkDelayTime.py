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
