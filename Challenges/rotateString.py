"""
Rotate String

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
"""

"""
Brute Force
For each rotation, do a check

Time: O(N^2)
Space: O(1)
"""
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == B:
            return True
        for i in range(len(A)):
            if A[i:] + A[:i] == B:
                return True
        return False
    
"""
Simple Check
Time: O(N^2)
Space: O(N)
"""
class Solution(object):
    def rotateString(self, A, B):
        return len(A) == len(B) and B in A+A


class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and B:
            return False
        max_rotate = len(A)
        count = 0
        while count <= max_rotate:
            if A == B:
                return True
            A = A[1:] + A[0]
            count += 1
        return False


class Solution2:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(0, len(A) + 1):
            if A[i:] + A[0:i] == B:
                return True

        return False
