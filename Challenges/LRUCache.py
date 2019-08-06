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

"""
O(1) Removal

O(N)的时间复杂度全败在了storage里面删除这块上面，我们如何实现storage中O(1)的Remove呢？遍历大家所学过的数据结构，能够满足删除O(1)并且有顺序机制的恐怕只有Linked List了。但链表的局限性是，我要删除特定节点确实是O(1)，但通过头结点遍历到需要删除的节点，是O(N)的操作。这时候我们自然会思考有没有办法用O(1)的时间找到节点。答案是我们完全可以把链表中节点的reference存储在字典的value里，这样我们可以用O(1)的时间寻找到节点，并且用O(1)的时间进行删除。

Linked List + Dictionary

Time: O(1) for both get/set API
"""
#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache(object):

    def __init__(self, capacity):
        self.dic = {}
        self.capacity = capacity
        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key):
        if key not in self.dic:
            return -1
        node = self.dic[key]
        self.remove(node)
        self.append(node)
        return node.val

    def put(self, key, value):
        if key in self.dic:
            self.remove(self.dic[key])
        node = Node(key, value)
        self.append(node)
        self.dic[key] = node

        if len(self.dic) > self.capacity:
            head = self.dummy_head.next
            self.remove(head)
            del self.dic[head.key]

    def append(self, node):
        tail = self.dummy_tail.prev
        tail.next = node
        node.prev = tail
        self.dummy_tail.prev = node
        node.next = self.dummy_tail

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev



"""
Q&A
Dummynode

因为我们可能要重复的进行删除，这种情况下往往要考虑头尾节点为空的状态，所以我们可以建立两个dummynode，分别处理这一类的edge case。

为什么要储存self.key

还有就是我们Node的定义和LC自带的有些区别，这里面要额外增加一个key的attribute，这个就是根据题意走了。因为当链表/字典的size大于咱的capacity，别忘了需要把head以及他在字典里的key删除掉的，至于这个key你从何而来，咱还是老老实实的存在Node里面吧。

为什么要Doubly Linked List, 为什么不用Singly Linked List

还有一个问题就是说，为什么是双向链表，为什么不用单链表。原因就是写起来轻松一点，不然要你去删除某个节点，并且只给你节点本身，你就得用一些奇淫技巧，嗯你懂得，就是LC的某道链表题。而且这还没完，你还得在字典里面更改对应的reference。

但换个角度想，单链表是否有他的好处，也有。因为我们双向链表中间多创建出来的k个previous指针累积了不少的memory overhead，所以这也是可以和面试官最后扫尾总结沟通的点。
"""

class DLinkedNode(): 
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        """
        Always add the new node right after head.
        """
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """
        Remove an existing node from the linked list.
        """
        prev = node.prev
        new = node.next

        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """
        Move certain node in between to the head.
        """
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """
        Pop the current tail.
        """
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        node = self.cache.get(key, None)
        if not node:
            return -1

        # move the accessed node to the head;
        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        node = self.cache.get(key)

        if not node: 
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1

            if self.size > self.capacity:
                # pop the tail
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # update the value.
            node.value = value
            self._move_to_head(node)

