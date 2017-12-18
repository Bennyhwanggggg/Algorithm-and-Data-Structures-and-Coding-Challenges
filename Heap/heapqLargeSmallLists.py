'''
Finding the Largest or Smallest N Items

Problem
You want to make a list of the largest or smallest N items in a collection.
'''

import heapq
import random

random.seed(10)
nums = random.sample(range(1,1000), 50)

print(nums) # [571, 429, 578, 206, 813, 823, 653, 161, 521, 328, 250, 952, 996, 45, 860, 603, 382, 284, 675, 457, 686, 662, 133, 768, 982, 969, 613, 5, 134, 941, 303, 366, 898, 315, 549, 436, 65, 584, 844, 157, 225, 413, 37, 497, 818, 658, 533, 855, 150, 567]

# Get the 5 largest numbers in a list
print(heapq.nlargest(5,nums)) # [996, 982, 969, 952, 941]

# Get the 5 smallest numbers in a list
print(heapq.nsmallest(5,nums)) # [5, 37, 45, 65, 133]


# Also can be used with key parameters. Important for dictionary structures. However, the key must point to comparable values e.g numbers
records = [ {'Team': 'Japan', 'Captain': 'Bob', 'Wins': 13},
            {'Team': 'Australia', 'Captain': 'Tim', 'Wins': 9},
            {'Team': 'USA', 'Captain': 'John', 'Wins': 3},
            {'Team': 'Canada', 'Captain': 'Tom', 'Wins': 5},
            {'Team': 'Mexico', 'Captain': 'Raul', 'Wins': 6}]

Strong =  heapq.nlargest(2, records, key = lambda w: w['Wins'])
print(Strong) # Japan and Australia details
Weak = heapq.nsmallest(2, records, key = lambda w: w['Wins'])
print(Weak) # USA and Canada details

# heappop pops from the element that is at top of the heap structure.
strongest = heapq.heappop(Strong)
print(strongest) # Japan's details

weakest = heapq.heappop(Weak)
print(weakest) # USA's detail
