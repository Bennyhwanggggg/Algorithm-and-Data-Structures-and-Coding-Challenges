"""
Maximum Length of Pair Chain

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
"""

"""
DP

Intuition

If a chain of length k ends at some pairs[i], and pairs[i][1] < pairs[j][0], we can extend this chain to a chain of length k+1.

Algorithm

Sort the pairs by first coordinate, and let dp[i] be the length of the longest chain ending at pairs[i]. When i < j and pairs[i][1] < pairs[j][0], we can extend the chain, and so we have the candidate answer dp[j] = max(dp[j], dp[i] + 1).

Time: O(N^2)
Space: O(N)
"""
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1] * len(pairs)
        
        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)
        return max(dp)
    
"""
Greedy

Intuition

We can greedily add to our chain. Choosing the next addition to be the one with the lowest second coordinate is at least better than a choice with a larger second coordinate.

Algorithm

Consider the pairs in increasing order of their second coordinate. We'll try to add them to our chain. If we can, by the above argument we know that it is correct to do so.

Time: O(N log(N))
Space: O(N)
"""
class Solution(object):
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = lambda x:x[1]):
            if cur < x:
                cur = y
                ans += 1
        return ans

