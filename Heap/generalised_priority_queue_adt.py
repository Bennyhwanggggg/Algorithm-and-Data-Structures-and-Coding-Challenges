'''
Written by Benny Hwang 02/11/2017 

 A max priority queue abstract data type to insert pairs of the form (datum, priority).
 If a pair is inserted with a datum that already occurs in the priority queue, then
 the priority is (possibly) changed to the (possibly) new value.
'''


class EmptyPriorityQueueError(Exception):
    def __init__(self, message):
        self.message = message


class PriorityQueue():
    min_capacity = 10

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None]*capacity
        self._length = 0
        self.locations = {}
        
    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def insert(self, element):
        datum = element[0]
        priority = element[1]        
        if datum in self.locations:
            self.change_priority(datum, priority)
            return
        if self._length + 1 == len(self._data):
            self._resize(2*len(self._data))
        self._length += 1        
        self._data[self._length] = [datum, priority]
        self.locations[datum] = self._length
        self._bubbleUp(self._length)

    def delete(self):
        if self.is_empty():
            raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
       
        # Swap the first element with the last one and then reduce length
        # then bubble down the first element
        top_datum = self._data[1][0]
        # remove from locations
        del self.locations[top_datum]

        self._data[1], self._data[self._length] = self._data[self._length], self._data[1]
        self._length -= 1
        if self.min_capacity // 2 <= self._length  <= len(self._data)//4:
            self._resize(len(self._data)//2)
        self._bubbleDown(1)
        return top_datum
            

    def _bubbleUp(self, i):
        # we bubble up an element if its parent (i//2) is smaller than i.
        # cannot bubble up if i is 1 since we will be at the top already (starting index is 1, as 0 is filled with None)
        if i > 1 and self._data[i][1] > self._data[i//2][1]:
            self._data[i], self._data[i//2] = self._data[i//2], self._data[i]
            self.locations[self._data[i//2][0]] = i//2
            self.locations[self._data[i][0]] = i
            self._bubbleUp(i//2)

    def _bubbleDown(self, i):
        child = 2*i
        if child < self._length and self._data[child][1] < self._data[child+1][1]:
            child += 1
        if child < self._length:
            self._data[child], self._data[i] = self._data[i], self._data[child]
            self.locations[self._data[child][0]] = child
            self.locations[self._data[i][0]] = i
            self._bubbleDown(child)

    def _resize(self, new_size):
            # change size of _data
         self._data = list(self._data[: self._length + 1]) + [None] * (new_size - self._length - 1)

    def change_priority(self, datum, priority):
        i = self.locations[datum]
        if priority > self._data[i][1]:
            self._data[i][1] = priority
            self._bubbleUp(i)
        if priority < self._data[i][1]:
            self._data[i][1] = priority
            self._bubbleDown(i)
            
