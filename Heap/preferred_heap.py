# Randomly generates N distinct integers with N provided by the user,
# inserts all these elements into a priority queue, and outputs a list
# L consisting of all those N integers, determined in such a way that:
# - inserting the members of L from those of smallest index of those of
#   largest index results in the same priority queue;
# - L is preferred in the sense that the last element inserted is as large as
#   possible, and then the penultimate element inserted is as large as possible, etc.
#
# Written by Benny Hwang 27/10/2017


import sys
from random import seed, sample

from priority_queue_adt import *

def reset_pq(original):
    
    tempQ = PriorityQueue()
    for e in original[1: ]:
        tempQ.insert(e)
    pq = tempQ

    return pq

def remove_largest_possible( target_index,testQ):
    global pq
    for index in reversed(target_index):
        if index == 1:
            val = pq.delete()
            pq.insert(val)
            if pq._data[ : len(pq) + 1] == testQ:
                pq.delete()
                return val
            pq = reset_pq(testQ)

        while index//2:
            parent_index = index//2
            pq._data[parent_index], pq._data[index] = pq._data[index], pq._data[parent_index]
            index = index//2

        val = pq.delete()
        possible_new = pq._data[ : len(pq) + 1]
        pq.insert(val)
        
        if pq._data[ : len(pq) + 1] == testQ:
            pq = reset_pq(possible_new)
            return val

        pq = reset_pq(testQ)
        

def get_route_to_root(current_last_pos):
    target_index = []
    target_index.append(current_last_pos)
    while current_last_pos//2:
        current_last_pos = current_last_pos//2
        target_index.append(current_last_pos)
    return target_index
       
def preferred_sequence():
    perferred_order = []
    while len(perferred_order)!= len(L):
        
        testQ = pq._data[ : len(pq) + 1]
        current_last_pos = len(pq._data[ : len(pq) + 1])-1
        target_index = get_route_to_root(current_last_pos)
        val = remove_largest_possible( target_index,testQ)
        perferred_order.append(val)

    return perferred_order[::-1]
    
    

try:
    for_seed, length = [int(x) for x in input('Enter 2 nonnegative integers, the second one '
                                                                             'no greater than 100: '
                                             ).split()
                       ]
    if for_seed < 0 or length > 100:
        raise ValueError
except ValueError:
    print('Incorrect input (not all integers), giving up.')
    sys.exit()    
seed(for_seed)
L = sample(list(range(length * 10)), length)
pq = PriorityQueue()
for e in L:
    pq.insert(e)
print('The heap that has been generated is: ')
print(pq._data[ : len(pq) + 1])
print('The preferred ordering of data to generate this heap by successsive insertion is:')
print(preferred_sequence())


