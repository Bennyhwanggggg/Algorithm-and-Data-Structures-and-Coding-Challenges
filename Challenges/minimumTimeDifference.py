"""
Minimum Time Difference

Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.
Example 1:
Input: ["23:59","00:00"]
Output: 1
Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
Accepted
30,121
Submissions
62,254
"""


"""
Time: O(nlogn) to sort the times
Space: O(n)
"""
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = []
        for time in timePoints:
            hr, mm = time.split(':')
            t = int(hr)*60 + int(mm)
            times.append(t)
        
        times.sort()
        res = float('inf')
        for i in range(1, len(times)):
            res = min(res, times[i]-times[i-1])
            if res == 0:
                return res
        if len(times) > 1:
            res = min(res, (24*60)+times[0] - times[-1])
        return res

