#!/bin/python3

import math
import os
import random
import re
import sys

'''
It has to do with the value of K.
When K is 1, every number is swapped with the subsequent number.
When K is 2, every pair is swapped with the subsequent pair.
When K is 3, every set of 3 numbers if swapped with the subsequent set of 3.
And so on.
'''

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    num = [i for i in range(1, n+1)]
    if not k:
        return ' '.join([str(e) for e in num])
    if n%(2*k):
        return '-1'
    for j in range(0, n//(2*k)):
        for i in range(1, k+1):
            num[j*2*k+i-1], num[j*2*k+i+k-1] = num[j*2*k+i+k-1], num[j*2*k+i-1]
        
    return ' '.join([str(e) for e in num])


def getAbsolutePermutation2(n, k):
  # K = 0 is always possible
  if k == 0:
    return ' '.join(str(x) for x in range(1, n + 1))
  # Odd values of K or when K is not a factor of N is not possible
  if n % 2 == 1 or n % k != 0:
    return -1
  
  ls = [x for x in range(1, n + 1)]
  
  # Begin swapping sets of numbers to generate the possible absolute permutation
  for i in range(0, n, k * 2):
    # The start of the first set of numbers
    start = i
    # End of first set, start of second set
    middle = i + k
    # The end of the second set of numbers
    end = i + k * 2
    
    # Swap the sets
    ls[start : middle], ls[middle : end] = ls[middle : end], ls[start : middle]
  # Check if the new list is a valid answer
  if all(abs(x - i - 1) == k for i,x in enumerate(ls)):
    return ' '.join(str(x) for x in ls)
  else:
    return -1
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        fptr.write(''.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
