'''
Heap Structure Priority Queue
Problem

You want to implement a queue that sorts items by a given priority and always returns
the item with the highest priority on each pop operation.
'''

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) # the -ve sign infront of priority is to make the module sort from the highest priority to the lowest. (Heapq module sorts from lowest to highest in value)
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def peekTop(self):
        return self._queue[0] # Will return a tuple with -priority, index, item
