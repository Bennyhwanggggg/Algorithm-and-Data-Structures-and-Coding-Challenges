"""
Merge Intervals

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

"""
Time: O(nlogn)
Space: O(n)
"""
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
