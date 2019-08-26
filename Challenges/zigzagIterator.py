"""
Zigzag Iterator

Given two 1d vectors, implement an iterator to return their elements alternately.

Example:

Input:
v1 = [1,2]
v2 = [3,4,5,6] 

Output: [1,3,2,4,5,6]

Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,3,2,4,5,6].
Follow up: What if you are given k 1d vectors? How well can your code be extended to such cases?

Clarification for the follow up question:
The "Zigzag" order is not clearly defined and is ambiguous for k > 2 cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic". For example:

Input:
[1,2,3]
[4,5,6,7]
[8,9]

Output: [1,4,8,2,5,9,3,6,7].
"""
"""
Queue
Time: O(1)
Space: O(N)
"""
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = collections.deque(v1)
        self.v2 = collections.deque(v2)
        self.call = 1

    def next(self):
        """
        :rtype: int
        """
        if not self.v1:
            res = self.v2.popleft()
        elif not self.v2:
            res = self.v1.popleft()
        elif self.call % 2 == 1:
            res = self.v1.popleft()
        else:
            res = self.v2.popleft()
        self.call += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v1) or len(self.v2)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

