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