"""
Sequence Reconstruction

Check whether the original sequence org can be uniquely reconstructed from the sequences in seqs. The org sequence is a permutation of the integers from 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common supersequence of the sequences in seqs (i.e., a shortest sequence so that all sequences in seqs are subsequences of it). Determine whether there is only one sequence that can be reconstructed from seqs and it is the org sequence.

Example 1:

Input:
org: [1,2,3], seqs: [[1,2],[1,3]]

Output:
false

Explanation:
[1,2,3] is not the only one sequence that can be reconstructed, because [1,3,2] is also a valid sequence that can be reconstructed.
Example 2:

Input:
org: [1,2,3], seqs: [[1,2]]

Output:
false

Explanation:
The reconstructed sequence can only be [1,2].
Example 3:

Input:
org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]

Output:
true

Explanation:
The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original sequence [1,2,3].
Example 4:

Input:
org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]

Output:
true
"""

"""
BFS/Topoligical sort
There should only be 1 starting node each level
Reconstruct
Time: O(N) N = number of sequence
"""
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        children = collections.defaultdict(set)
        parents = collections.defaultdict(set)
        nodes = set()
        for s in seqs:
            for i in range(len(s)):
                nodes.add(s[i])
                if i > 0:
                    parents[s[i]].add(s[i-1])
                if i < len(s)-1:
                    children[s[i]].add(s[i+1])
                    
        stack = [n for n in nodes if len(parents[n]) == 0]
        
        count = len(stack)
        ans = []
        
        while count == 1:
            curr = stack.pop()
            count -= 1
            ans.append(curr)
            nodes.remove(curr)
            for child in children[curr]:
                parents[child].remove(curr)
                if len(parents[child]) == 0:
                    stack.append(child)
                    count += 1
        return not nodes and ans == org

