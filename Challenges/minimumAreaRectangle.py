"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

 

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Note:

1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""

"""
First, use two dict to record all points according to it's position.
dx[i] record all points which located at x=i
dy[i] record all points which located at y=i

for instance, points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
dx = {1: [1,3], 2:[2], 3:[1,3]}
dy = {1: [1,3], 2:[2], 3:[1,3]}

Then, follow these steps:

find one x in dx
find y1,y2 in dx[x]
find x1 in dy[y1]
judge (x1,y2) in points

Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def minAreaRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        seen = set(map(tuple, points))
        dx = collections.defaultdict(list)
        dy = collections.defaultdict(list)
        for x, y in points:
            dx[x].append(y)
            dy[y].append(x)
        
        res = float('inf')
        
        """
        (x1, y2)        (x2, y2)
        
        
        (x1, y1)        (x2, y1)
        """
        for x1 in sorted(dx.keys()): # 1. find x in dx
            for i in range(len(dx[x1])):  # 2. find y1, y2 in dx[x]
                y1 = dx[x1][i]
                for j in range(i+1, len(dx[x1])):
                    y2 = dx[x1][j]
                    for x2 in dy[y2]: # 3. find x1 in dy[y2]
                        if x2 <= x1: # always make x1 in the left side
                            continue
                        if (x2, y1) in seen:
                            res = min(res, abs(x1-x2) * abs(y1-y2))
        return res if res != float('inf') else 0
        
class Solution(object):
    def minAreaRect(self, points):
        columns = collections.defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        lastx = dict()
        ans = float('inf')

        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in xrange(j):
                    y1 = column[i]
                    if (y1, y2) in lastx:
                        ans = min(ans, (x - lastx[y1,y2]) * (y2 - y1))
                    lastx[y1, y2] = x
        return ans if ans < float('inf') else 0

