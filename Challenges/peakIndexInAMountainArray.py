"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""

"""
Linear Scan:
Time: O(n)
Space: O(1)
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        peak = 0
        res = -1
        for i in range(1, len(A)-1):
            if A[i] > A[i-1] and A[i] > A[i+1]:
                if A[i] > peak:
                    res = i
                    peak = A[i]
        return res
    
"""
Simply find largest value's index
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
    
"""
Binary Search
Time: O(log(n))
Space: O(1)
Works as there is only one mountain and the array is strictly increasing 
until it reaches the mountain peak. THerefore, the comparison A[i] < A[i+1] will turn false
when we reach the peak
"""
class Solution(object):
    def peakIndexInMountainArray(self, A):
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mi = (lo + hi) // 2
            if A[mi] < A[mi + 1]:
                lo = mi + 1
            else:
                hi = mi
        return lo
