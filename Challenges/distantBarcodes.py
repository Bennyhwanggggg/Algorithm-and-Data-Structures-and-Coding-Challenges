"""
Distant Barcodes

In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].

Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.

 

Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 

Note:

1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000

"""

"""
PQ
Time: O(Nlog(N))
Space: O(N)
"""
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counts = collections.Counter(barcodes)
        
        pq = []
        for n in counts:
            heapq.heappush(pq, (-counts[n], n))
        
        res = []
        while len(pq) > 1:
            ct1, n1 = heapq.heappop(pq)
            ct2, n2 = heapq.heappop(pq)
            if not res or res[-1] != n1:
                res.extend([n1, n2])
            else:
                res.extend([n2, n1])
            ct1 += 1
            ct2 += 1 
            if ct1 < 0:
                heapq.heappush(pq, (ct1, n1))
            if ct2 < 0:
                heapq.heappush(pq, (ct2, n2))
        
        if pq:
            res.append(pq[0][1])
        return res
    
"""
Use Odd even pos
Time: O(N)
Space: O(1)
"""
def rearrangeBarcodes(self, packages):
        i, n = 0, len(packages)
        res = [0] * n
        for k, v in collections.Counter(packages).most_common():
            for _ in xrange(v):
                res[i] = k
                i += 2
                if i >= n: 
                    i = 1
        return res
                

