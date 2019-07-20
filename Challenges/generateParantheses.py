"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


Time complexity of backtracking solution:
The way I like to think about the runtime of backtracking algorithms is O(b^d), where b is the branching factor and d is the maximum depth of recursion.

Backtracking is characterized by a number of decisions b that can be made at each level of recursion. If you visualize the recursion tree, this is the number of children each internal node has. You can also think of b as standing for "base", which can help you remember that b is the base of the exponential.

If we can make b decisions at each level of recursion, and we expand the recursion tree to d levels (ie: each path has a length of d), then we get b^d nodes. Since backtracking is exhaustive and must visit each one of these nodes, the runtime is O(b^d).
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if not n:
            return res
        
        def helper(res, curr, nOpening, nClosing):
            if nOpening > nClosing:
                return
            if nOpening == 0 and nClosing == 0:
                res.append(curr)
                return
            if nOpening > 0:
                helper(res, curr + '(', nOpening-1, nClosing)
            if nClosing > 0:
                helper(res, curr + ')', nOpening, nClosing-1)
        
        helper(res, '', n, n)
        return res
                    

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if not n:
            return res

        def helper(res, s, left, right):
            if left > right:
                return
            if left == 0 and right == 0:
                res.append(s)
                return
            if left > 0:
                helper(res, s + "(", left - 1, right)
            if right > 0:
                helper(res, s + ")", left, right - 1)

        helper(res, "", n, n)
        return res
