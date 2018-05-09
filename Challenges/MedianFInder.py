class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort(self.values, num)

    def findMedian(self):
        """
        :rtype: float
        """
        values_length = len(self.values)
        index = values_length // 2

        if values_length % 2 == 0:
            return (self.values[index - 1] + self.values[index]) / 2
        else:
            return float(self.values[index])

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()