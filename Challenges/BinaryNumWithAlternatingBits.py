class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        prev, curr = None, None
        while n>0:
            if prev is None:
                prev = n%2
                n //= 2
                continue
            else:
                curr = n%2
                n //= 2
            if curr == prev:
                return False
            prev = curr
        return True