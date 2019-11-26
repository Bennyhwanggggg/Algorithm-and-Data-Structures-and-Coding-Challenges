"""
Prime Palindrome

Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
 

Note:

1 <= N <= 10^8
The answer is guaranteed to exist and be less than 2 * 10^8.
"""

"""
construct palindromes first and then check if prime

Time: O(N)
"""
class Solution:
    def primePalindrome(self, N: int) -> int:
        ndigits = len(str(N))
        while True:
            for x in self.palindromes(ndigits):
                if x >= N and self.isPrime(x):
                    return x
            ndigits += 1
            
    def palindromes(self, n):
        if n == 1:
            for i in range(10):
                yield i
        elif n % 2 == 0:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                s = str(i)
                yield int(s + s[::-1])
        else:
            d = n // 2
            for i in range(10**(d-1), 10**d):
                s = str(i)
                for j in range(10):
                    yield int(s + str(j) + s[::-1])
                    
    def isPrime(self, x):
        if x == 1:
            return False
        if x == 2:
            return True
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
        return True



class Solution:
    def primePalindrome(self, N: int) -> int:
        ndigits = len(str(N))
        if N == 1:
            return 2
        if N <=3:
            return N
        elif N <= 5:
            return 5
        elif N <= 7:
            return 7
        elif N <= 11:
            return 11
        while True:
            for x in self.palindromes(ndigits):
                if x >= N and self.isPrime(x) :
                    return x
            ndigits+=1

    def palindromes(self, n):
        l = n // 2
        for i in range(10**(l-1), 10**l):
            s = str(i)
            for j in range(10):
                yield int(s + str(j) +  s[::-1])

    def isPrime(self, x):
        if x == 1:
            return False
        if x == 2:
            return True
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
        return True
