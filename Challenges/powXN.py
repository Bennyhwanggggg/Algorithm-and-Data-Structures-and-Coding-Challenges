"""
Implement pow(x, n), which calculates x raised to the power n (x^n).
"""

"""
Not allowed??
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        return x**n


class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n < 0:
            x = 1/x
            n = -n
            
        ans = 1
        for i in range(n):
            ans *= x
        
        return ans

    
"""
Fast Power Recursive
Time: O(log n), each time we apply the formulat, n is reduced by half.
Space: O(log n) storing log n number of result

if n is even, we can use the formula (x^n)^2 = x^(2n)
if n is odd, we can use A*A*x
"""
class Solution(object):
    def myPow(self, x, n):
        x = 1/x if n < 0 else x
        n = -n if n < 0 else n
        return self.fastPow(x, n)
    
    def fastPow(self, x, n):
        if n == 0:
            return 1.0
        half = self.fastPow(x, n/2)
        if not n%2:
            return half * half
        return half*half*x

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1
        elif n < 1:
            return 1 / (self.myPow(x, -n))
        if n % 2:
            return x * self.myPow(x, n - 1)
        else:
            return self.myPow(x * x, n / 2)
