"""
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.
"""

class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i] == i:
                return i
        return -1
    
class Solution:
    def fixedPoint(self, a):
        if not a:
            return -1

        i = 0
        j = len(a) - 1

        f = -1 if a[0] > 0 else -1 # is D[i] is decreasing or increasing

	    # what follows - just a binary search
        while i <= j:
            m = i + (j - i) // 2

            d = a[m] - m
            if d == 0:
                return m
            elif d * f > 0:
                i = m + 1
            else:
                j = m - 1

        return -1
