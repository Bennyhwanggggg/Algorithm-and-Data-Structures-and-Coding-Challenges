class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        from collections import deque

        self.total = 0.0
        self.size = size
        self.curr_size = 0
        self.q = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.total += val
        self.q.append(val)
        if self.curr_size < self.size:
            self.curr_size += 1
            return self.total / self.curr_size
        else:
            self.total -= self.q.popleft()
            return self.total / self.size


import collections


class MovingAverage:

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = collections.deque([], maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.nums.append(val)
        return sum(self.nums) / len(self.nums)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)