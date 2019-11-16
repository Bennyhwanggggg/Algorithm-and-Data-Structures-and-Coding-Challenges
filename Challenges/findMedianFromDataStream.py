"""
Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.
 

Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 

Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
"""

"""
Two heap
Time: O(log(n)) insert, O(1) find
Space: O(n)
"""
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = []  # store the small half, top is the largest in the small part
        self.large = []  # store the large half, top is the smallest in the large part

    def addNum(self, num: int) -> None:
        if len(self.small) == 0:
            heapq.heappush(self.small, -num)
            return
        if num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # balance
        if len(self.small) - len(self.large) >= 2:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) - len(self.small) >= 2:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0])/2
        return -self.small[0] if len(self.small) > len(self.large) else self.large[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# O(NlogN) worst one
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        length = len(self.nums)
        if length%2:
            return self.nums[length//2]
        else:
            return (self.nums[length//2] + self.nums[(length//2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# insertion sort, time: O(n) + O(log(n))
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
