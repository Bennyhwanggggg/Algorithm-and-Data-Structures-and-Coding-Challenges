"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2147483648 or x < -2147483648:
            return 0
        m = 1 if x >= 0 else -1
        
        x = x*m
        
        x = int(''.join(list(str(x))[::-1]))
        if x > 2147483648 or x < -2147483648:
            return 0
        return x*m
        
        
class Solution(object):
    def reverse(self, x):
        result = 0
        symbol = 1
        
        if x < 0:
            symbol = -1
            x = -x

        while x:
            result = result * 10 + x % 10
            x /= 10
            
        return 0 if result > pow(2,31) else result * symbol



class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        m = -1 if x < 0 else 1
        x = x * m

        n = 0
        while x > 0:
            n = (n * 10) + (x % 10)
            x = x // 10

        if n > 0x7FFFFFFF:
            return 0

        return n * m
