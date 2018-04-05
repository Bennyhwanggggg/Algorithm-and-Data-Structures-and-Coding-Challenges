# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        newStart = newInterval.start
        newEnd = newInterval.end
        results = []
        i = 0
        while i < len(intervals):
            if newStart <= intervals[i].end:
                if newEnd < intervals[i].start:
                    break
                newStart = min(newStart, intervals[i].start)
                newEnd = max(newEnd, intervals[i].end)
            else:
                results.append(intervals[i])
            i += 1

        results.append([newStart, newEnd])
        results.extend(intervals[i:])
        return results


