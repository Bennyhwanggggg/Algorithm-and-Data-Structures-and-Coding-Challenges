"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

"""
Time: O(1)
Space: O(n) where n = size
Note: python append is O(1)
"""
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.nums = collections.deque(maxlen=size)
        self.curr_sum = 0
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.curr_sum += val
        if len(self.nums) == self.size:
            self.curr_sum -= self.nums[0]
        self.nums.append(val)
        return self.curr_sum/len(self.nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

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
