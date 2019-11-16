"""
Reorganize String

Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""
Note:

S will consist of lowercase letters and have length in range [1, 500].
"""

"""
Greedy with Heap 
Time: O(Nlog(A))
Space: O(A) A = 26 (alphabets)
"""
class Solution:
    def reorganizeString(self, S: str) -> str:
        
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S)+1)/2 for nc, x in pq):
            return ''
        
        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            if not ans or ch1 != ans[-1]:
                ans.extend([ch1, ch2])
            else:
                ans.extend([ch2, ch1])
            if nct1 + 1 != 0:
                heapq.heappush(pq, (nct1+1, ch1))
            if nct2 + 1 != 0:
                heapq.heappush(pq, (nct2+1, ch2))
        
        return ''.join(ans) + (pq[0][1] if pq else '')

