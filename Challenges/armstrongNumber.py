"""
Armstrong Number

The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

Given a positive integer N, return true if and only if it is an Armstrong number.

 

Example 1:

Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
Example 2:

Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.
 

Note:

1 <= N <= 10^8
"""
class Solution:
    def isArmstrong(self, N: int) -> bool:
        armstrong = 0
        start = N
        digits = len(str(N))
        while N > 0:
            N, i = divmod(N, 10)
            armstrong += i**digits

        return armstrong == start
    
class Solution:
    def isArmstrong(self, N: int) -> bool:
        n_str = str(N)
        k = len(n_str)
        return sum(int(i)**k for i in n_str) == N
    
class Solution:
    def isArmstrong(self, N: int) -> bool:
        length = len(str(abs(N)))
        temp = N
        sum = 0
        while temp > 0:
            digit = temp % 10
            temp = temp // 10
            sum += digit**length

        return sum == N

