"""
Given a set of points in the xy-plane, determine the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the x and y axes.

If there isn't any rectangle, return 0.
"""


"""
Iterate Centers

Intuition

Consider opposite points AC and BD of a rectangle ABCD. They both have the same center O, which is the midpoint of AC and the midpoint of AB; and they both have the same radius dist(O, A) == dist(O, B) == dist(O, C) == dist(O, D). Notice that a necessary and sufficient condition to form a rectangle with two opposite pairs of points is that the points must have the same center and radius.

Motivated by that result, let's classify each pair of points PQ by their center C = the midpoint of PQ, and the radius r = dist(P, C). Our strategy is to brute force on pairs of points with the same classification.

Algorithm

For each pair of points, classify them by center and radius. We only need to record one of the points P, since the other point is P' = 2 * center - P (using vector notation).

For each center and radius, look at every possible rectangle (two pairs of points P, P', Q, Q'). The area of this rectangle dist(P, Q) * dist(P, Q') is a candidate answer.


Some pre-knowledge

Cross Product ---> c_prod(v1, v2) = x1y2 - x2y1
Area formula in Coordinates ---->area(v1, v2) = abs(c_prod) (v1, v2 is the vector of 2 vertical edge of the rectangle)
Middle point formula ----> mid(p1, p2) = ((x1+x2)/2, (y1+y2)/2)
Distance formula ----> dist(p1, p2) = SQRT ( (x1-x2)**2 + (y1-y2)**2 )

Time: O(N^2)
Space: O(N)
"""
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        dic = collections.defaultdict(list)
        
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):
                pi = points[i]
                pj = points[j]
                
                mx, my = (pi[0] + pj[0], pi[1] + pj[1])
                
                dia_sq = (pi[0] - pj[0]) ** 2 + (pi[1] - pj[1]) ** 2
                
                dic[mx, my, dia_sq].append(pi)
        
        ans = float('inf')
                        
        for (mx, my, _), lst in dic.items():
            for i in range(len(lst)-1):
                for j in range(i+1, len(lst)):
                    pi = lst[i]
                    pj = lst[j]
                    
                    neg_pj = [mx - pj[0], my - pj[1]]
                    
                    x1, y1 = pj[0] - pi[0], pj[1] - pi[1]
                    x2, y2 = neg_pj[0] - pi[0], neg_pj[1] - pi[1]
                                        
                    area = abs(x1 * y2 - x2 * y1)
                    
                    ans = min(area, ans)
                    
        return float(ans) if ans != float('inf') else 0

class Solution:
    def minAreaFreeRect(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        n = len(points)
        d = collections.defaultdict(list)

        for i in range(n - 1):
            pi = points[i]
            for j in range(i + 1, n):
                pj = points[j]
                length = ((pi[0] - pj[0]) ** 2) + ((pi[1] - pj[1]) ** 2)
                cx = (pi[0] + pj[0]) / 2.0
                cy = (pi[1] + pj[1]) / 2.0
                d[(length, cx, cy)].append((i, j))

        res = float("inf")
        for ls in d.values():
            length = len(ls)
            for i in range(length - 1):
                p0, p2 = points[ls[i][0]], points[ls[i][1]]
                for j in range(i + 1, length):
                    p1, p3 = points[ls[j][0]], points[ls[j][1]]
                    d1 = math.sqrt((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2)
                    d2 = math.sqrt((p0[0] - p3[0]) ** 2 + (p0[1] - p3[1]) ** 2)
                    res = min(res, d1 * d2)

        return res if res != float("inf") else 0

