"""
Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

"""
The Greedy approach just discussed was based on choosing intervals greedily based on the starting points. But in this approach, we go for choosing points greedily based on the end points. For this, firstly we sort the given intervals based on the end points. Then, we traverse over the sorted intervals. While traversing, if there is no overlapping between the previous interval and the current interval, we need not remove any interval. But, if an overlap exists between the previous interval and the current interval, we always drop the current interval.

Case 1:

The two intervals currently considered are non-overlapping:

In this case, we need not remove any interval and for the next iteration the current interval becomes the previous interval.

Case 2:

The two intervals currently considered are overlapping and the starting point of the later interval falls before the starting point of the previous interval:

In this case, as shown in the figure below, it is obvious that the later interval completely subsumes the previous interval. Hence, it is advantageous to remove the later interval so that we can get more range available to accommodate future intervals. Thus, previous interval remains unchanged and the current interval is updated.

Case 3:

The two intervals currently considered are overlapping and the starting point of the later interval falls before the starting point of the previous interval:

In this case, the only opposition to remove the current interval arises because it seems that more intervals could be accommodated by removing the previous interval in the range marked by A. But that won't be possible as can be visualized with a case similar to Case 3a and 3b shown above. But, if we remove the current interval, we can save the range B to accommodate further intervals. Thus, previous interval remains unchanged and the current interval is updated.

To explain how it works, again we consider every possible arrangement of the intervals.

Time complexity : O(nlog(n)). Sorting takes O(nlog(n)) time.

Space complexity : O(1). No extra space is used.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x: x[1])
        
        end = intervals[0][1]
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                end = intervals[i][1]
                count += 1
        return len(intervals) - count


"""
Case 1:

The two intervals currently considered are non-overlapping:

In this case, we need not remove any interval and we can continue by simply assigning the prevprev pointer to the later interval and the count of intervals removed remains unchanged.

Case 2:

The two intervals currently considered are overlapping and the end point of the later interval falls before the end point of the previous interval:

In this case, we can simply take the later interval. The choice is obvious since choosing an interval of smaller width will lead to more available space labelled as AA and BB, in which more intervals can be accommodated. Hence, the prevprev pointer is updated to current interval and the count of intervals removed is incremented by 1.

Case 3:

The two intervals currently considered are overlapping and the end point of the later interval falls after the end point of the previous interval:

In this case, we can work in a greedy manner and directly remove the later interval.
"""
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        end = intervals[0][1]
        prev, count = 0, 0
        for i in range(1, len(intervals)):
            if intervals[prev][1] > intervals[i][0]: # if previous ends after current start
                if intervals[prev][1] > intervals[i][1]: # if prevous ends after current end
                    prev = i # make the current one the new prev as prev is removed as it is a larger interval and removing it will allow more intervals to be fitted in
                count += 1 # update count due to overlapping
            else:
                prev = i # update prev to current and count of intervals don't change
        return count

