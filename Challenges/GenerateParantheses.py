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