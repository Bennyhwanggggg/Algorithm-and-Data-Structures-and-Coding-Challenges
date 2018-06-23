#!/bin/python3

import math
import os
import random
import re
import sys


def isPattern(G, row, col, P):
    for r in range(len(P)):
        for c in range(len(P[0])):
            if row+r >= len(G) or col+c >= len(G[0]) or P[r][c] != G[row+r][col+c]:
                return False
    return True


# Complete the gridSearch function below.
def gridSearch(G, P):
    validPattern = True
    for row in range(len(G)):
        for col in range(len(G[0])):
            if G[row][col] == P[0][0] and isPattern(G, row, col, P):
                return 'YES'
    return 'NO'
                
                        
                        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        RC = input().split()

        R = int(RC[0])

        C = int(RC[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        rc = input().split()

        r = int(rc[0])

        c = int(rc[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
