"""
Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""

"""
Time and Space: O(N)
"""
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        seen = dict()
        ans = 0
        for a, b in dominoes:
            if (a, b) in seen:
                ans += seen[(a, b)]
            if (a, b) != (b, a) and (b, a) in seen:
                ans += seen[(b, a)]
            seen[(a, b)] = seen.get((a, b), 0) + 1
        return ans
