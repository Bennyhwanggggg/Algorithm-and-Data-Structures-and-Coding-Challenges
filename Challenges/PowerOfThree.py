"""
Given an integer, write a function to determine if it is a power of three.
"""

"""
Naive
Time: O(log_3(n))
Space: O(1)
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n%3 == 0:
            n /= 3
        
        return n == 1
    
"""
Math sol but math.log time complexity unknown and depends on the language
"""
public class Solution {
    public boolean isPowerOfThree(int n) {
        return (Math.log10(n) / Math.log10(3)) % 1 == 0;
    }
}

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        while not n % 3:
            n = n / 3

        return True if n == 1 else False
