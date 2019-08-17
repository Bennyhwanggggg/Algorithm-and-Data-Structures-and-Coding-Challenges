"""
Shortest Distance To A Character

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
"""

"""
BFS
Time: O(N)
Space: O(N)
"""
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        res = [float('inf')]*len(S)
        queue = collections.deque()
        for idx, l in enumerate(S):
            if l == C:
                queue.append((idx, 0))
        
        while queue:
            idx, dist = queue.popleft()
            res[idx] = min(res[idx], dist)
            if idx > 0 and res[idx-1] == float('inf'):
                queue.append((idx-1, dist+1))
            if idx < len(S)-1 and res[idx+1] == float('inf'):
                queue.append((idx+1, dist+1))
                
        return res

