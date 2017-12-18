'''
Written by Eric Martin modified by Benny Hwang

 A priority queue abstract data type.
'''


class EmptyPriorityQueueError(Exception):
    def __init__(self, message):
        self.message = message

    
class PriorityQueue():
    min_capacity = 20

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None] * capacity
        self._length = 0
        
    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def insert(self, element):
        if self._length + 1 == len(self._data):
            self._resize(2 * len(self._data))
        self._length += 1
        self._data[self._length] = element
        self._bubble_up(self._length)

    def delete(self):
        if self.is_empty():
            raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
        max_element = self._data[1]
        self._data[1], self._data[self._length] = self._data[self._length], self._data[1]
        self._length -= 1
        # When the priority queue is one quarter full, we reduce its size to make it half full,
        # provided that it would not reduce its capacity to less than the minimum required.
        if self.min_capacity // 2 <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._bubble_down(1)
        return max_element
        
    def _bubble_up(self, i):
        if i > 1 and self._data[i] > self._data[i // 2]:
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]
            self._bubble_up(i // 2)

    def _bubble_down(self, i):
        child = 2 * i
        if child < self._length and self._data[child + 1] > self._data[child]:
            child += 1
        if child <= self._length and self._data[i] < self._data[child]:
            self._data[child], self._data[i] = self._data[i], self._data[child]
            self._bubble_down(child)

    def _resize(self, new_size):
        self._data = list(self._data[: self._length + 1]) + [None] * (new_size - self._length - 1)

