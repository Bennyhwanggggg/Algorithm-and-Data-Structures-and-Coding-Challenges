'''
Written by Benny Hwang 25/10/2017

 The prime numbers between 2 and 12 (both included) are: 2, 3, 5, 7, 11
 The gaps between successive primes are: 0, 1, 1, 3.
 Hence the maximum gap is 3.
'''

import sys
from math import sqrt


def f(a, b):
    if a <= 0 or b < a:
        sys.exit()
    max_gap = 0

    gaps = [None] * (b+1)
    for n in range(a, b+1):
        if is_prime(n):
            gaps[n] = 1

    primes = [pos for pos, val in enumerate(gaps) if val == 1]
    
    for e in range(1, len(primes)):
        current_gap = primes[e] - primes[e-1] - 1
        if current_gap > max_gap:
            max_gap = current_gap
    
    print('The maximum gap between successive prime numbers in that interval is', max_gap)
                
            
    
def is_prime(n):
    if n > 2:
        return all(n%i for i in range(2,n))
    return False


