import sys
from itertools import accumulate
from collections import Counter

n1,n2,n3 = input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = [int(h1_temp) for h1_temp in input().strip().split(' ')]
h2 = [int(h2_temp) for h2_temp in input().strip().split(' ')]
h3 = [int(h3_temp) for h3_temp in input().strip().split(' ')]

h1c, h2c, h3c = [list(accumulate(reversed(l))) for l in (h1, h2, h3)]
total_stack = h1c + h2c + h3c
counter_stack = Counter(total_stack)
try:
    print(max(i[0] for i in counter_stack.items() if i[1] == 3))
except:
    print(0)