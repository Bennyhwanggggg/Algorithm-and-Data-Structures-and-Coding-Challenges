# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        start, end, result = [], [], []
        for interval in intervals:
            st, en = interval.start, interval.end
            start.append(st)
            end.append(en)

        start.sort()
        end.sort()

        i = 0
        while i < len(intervals):
            st = start[i]
            while i < len(intervals) - 1 and start[i + 1] <= end[i]:
                i += 1
            en = end[i]
            result.append([st, en])
            i += 1
        return result
