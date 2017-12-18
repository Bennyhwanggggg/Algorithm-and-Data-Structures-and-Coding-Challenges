# Written by Benny Hwang 28/10/2017
from linked_list_adt import *

# merge sorted lists by number size then return the head
def merge(L1, L2):
    if not L1.head and L2.head:
        return L2.head
    if not L2.head and L1.head:
        return L1.head
    if not L2.head and not L1.head:
        return

    # if the head value of L1 is larger than L2, we want to switch the two lists
    if L1.head.value > L2.head.value:
        temp = L2.head
        L2.head = L1.head
        L1.head = temp

    currentL1 = L1.head
    currentL2 = L2.head

    # Since we have already checked the first value of L1, proceed with nextnode
    while currentL1.next_node and currentL2:
        # move to the next number in L1 that is larger than currentL2
        while currentL1.next_node and currentL1.next_node.value < currentL2.value:
            currentL1 = currentL1.next_node

        # once we have reached that point, we want to insert that L2 into L1
        # and move L1 to next node and L2 to next node
        # we also need to delink the removed node from its original list
        nextL2 = currentL2.next_node
        nextL1 = currentL1.next_node
        currentL1.next_node = currentL2
        currentL2.next_node = None
        currentL2 = nextL2
        currentL1.next_node.next_node = nextL1
        currentL1 = currentL1.next_node
    return L1.head
   

# merge two unsorted list by taking 1 from each each time then return the head
def merge_two(L1, L2):
    if not L1.head and L2.head:
        return L2.head
    if not L2.head and L1.head:
        return L1.head
    if not L2.head and not L1.head:
        return

    currentL1 = L1.head
    currentL2 = L2.head

    while currentL1.next_node and currentL2.next_node :
        nextL2 = currentL2.next_node
        nextL1 = currentL1.next_node
        currentL1.next_node = currentL2
        currentL2.next_node = None
        currentL2 = nextL2
        currentL1.next_node.next_node = nextL1
        currentL1 = currentL1.next_node.next_node

    if currentL2:
        currentL1.next_node = currentL2

    return L1.head
        
