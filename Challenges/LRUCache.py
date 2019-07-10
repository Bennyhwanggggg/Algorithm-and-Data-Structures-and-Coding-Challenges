"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""


"""
Ordered dictionary
Intuition

We're asked to implement the structure which provides the following operations in \mathcal{O}(1)O(1) time :

Get the key / Check if the key exists

Put the key

Delete the first added key

The first two operations in \mathcal{O}(1)O(1) time are provided by the standard hashmap, and the last one - by linked list.

There is a structure called ordered dictionary, it combines behind both hashmap and linked list. In Python this structure is called OrderedDict and in Java LinkedHashMap.
"""
from collections import OrderedDict
class LRUCache():

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return - 1
        
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Brute force
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.history = collections.deque()
        
    def get(self, key: int) -> int:
        if key in self.cache.keys():
            self.updateHistory(key)
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if len(self.cache.keys()) > self.capacity:
            toRemove = self.history.popleft()
            self.cache.pop(toRemove)
        self.updateHistory(key)
        
    def updateHistory(self, newMove):
        if newMove in self.history:
            self.history.remove(newMove)
        self.history.append(newMove)
        
        


# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)
