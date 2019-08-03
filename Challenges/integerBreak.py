"""
Integer Break

Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""

"""
The key for this problem is that we need to break the number to 2s, 3s and 4s.
First we need to know a fact that,if a,b > 3, |a-b| <= 1, then a*b>=a+b.

So, if n = a + b, a = a1+a2, b=b1+b2, we should break n to a1+a2+b1+b2, |a1-a2|<1 and |b1-b2|<1 instead of a + b, because a1*a2>a, b1*b2>b. However, we shall stop when we get a 3 or 2, so what we shall do is to find the list of 3 and 2.

You may have noticed why the 4 appeared. 'Cause if we break 4, we get 2+2, and 2+2 = 2*2, so it's the same with the condition that we get two 2s.

Time: O(N)
Space: O(1)
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        list_of_3s = [3]*(n//3)
        mod_3 = n%3
        if mod_3 == 1:
            list_of_3s[0] += 1
        elif mod_3 == 2:
            list_of_3s.append(2)
            
        res = 1
        for n in list_of_3s:
            res *= n
        return res

