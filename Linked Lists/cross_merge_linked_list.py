# Generates two linked lists of a length determined by user input,
# consisting of random nonnegative integers whose upper bound is also determined
# by user input, and merge the linked list using the two different way described in mergeLinkList
#
# Written by Benny Hwang 28/10/2017


import sys
from random import seed, randrange
import mergeLinkList 
from linked_list_adt import LinkedList

try:
    for_seed, length, upper_bound = [int(i) for i in input('Enter three nonnegative integers: '
                                                          ).split()
                                    ]                                     
    if for_seed < 0 or length < 0 or upper_bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
LL1 = LinkedList(sorted([randrange(upper_bound + 1) for _ in range(length+randrange(4))]))
LL2 = LinkedList(sorted([randrange(upper_bound + 1) for _ in range(length+randrange(4))]))
print("List 1: ")
LL1.print()
print("List 2: ")
LL2.print()

LL3 = mergeLinkList.merge(LL1, LL2)
print("Merged method 1 linked list")
while LL3:
    print(LL3.value, end = ' ')
    LL3 = LL3.next_node

print()
LL4 = LinkedList(sorted([randrange(upper_bound + 1) for _ in range(length+randrange(4))]))
LL5 = LinkedList(sorted([randrange(upper_bound + 1) for _ in range(length+randrange(4))]))
print("List 3: ")
LL4.print()
print("List 4: ")
LL5.print()
LL6 = mergeLinkList.merge_two(LL4, LL5)
print("Merged method 2 linked list")
while LL6:
    print(LL6.value, end = ' ')
    LL6 = LL6.next_node
