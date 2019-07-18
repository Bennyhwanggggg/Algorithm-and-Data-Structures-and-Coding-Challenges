"""
Valid Mountain Array

Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""

"""
One pass

Intuition

If we walk along the mountain from left to right, we have to move strictly up, then strictly down.

Algorithm

Let's walk up from left to right until we can't: that has to be the peak. We should ensure the peak is not the first or last element. Then, we walk down. If we reach the end, the array is valid, otherwise its not.

Time: O(n)
Space: O(1)
"""
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        valid = False
        if len(A) < 3:
            return valid
        
        peak = max(A)
        i = 1
        is_increasing = True
        while i < len(A):
            if A[i] > A[i-1] and not is_increasing:
                return False
            elif A[i] < A[i-1] and is_increasing:
                return False
            elif A[i] == A[i-1]:
                return False
            if A[i] == peak:
                is_increasing = False
            i += 1
                
        return True if peak != A[i-1] else False
       
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
