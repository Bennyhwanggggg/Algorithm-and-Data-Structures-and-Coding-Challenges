#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_num = float('inf')
    max_num = -float('inf')
    total_sum = sum(arr)
    for n in arr:
        result = total_sum - n
        min_num = min(result, min_num)
        max_num = max(result, max_num)
    
    print('{} {}'.format(min_num, max_num))
    return

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

