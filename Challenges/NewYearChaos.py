#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    ans = 0 
    for i, v in enumerate(q):
        # check if the queue is too chaotic
        if (v - 1) - i > 2:
            print('Too chaotic')
            return
        # only need to count number of people who over take the person
        for j in range(max(0, v-2), i):
            if q[j] > v:
                ans += 1
        '''
        # bubble sorting to find the answer
        for i in xrange(0, lastIndex):
            for j in xrange(0, lastIndex):
                comps += 1
                if queue[j] > queue[j+1]:
                    temp = queue[j]
                    queue[j] = queue[j+1]
                    queue[j+1] = temp
                    swaps += 1
                    swaped = True
            
            if swaped:
                swaped = False
            else:
                break
        '''
    print(ans)
    return

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
