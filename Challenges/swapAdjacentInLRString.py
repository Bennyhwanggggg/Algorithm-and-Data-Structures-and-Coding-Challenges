"""
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
"""

"""
Two pointers

First notice that L can only move forward while R can only move backward. Therefore, start's L can never move to the position in end as it can only move forward. Vice versa, R  as well.
Use two pointers on each string. Move to the first non-X position and check the two elements. 
Return False straightaway because no matter if it is L or R, they can only exchange position with X and L and R cannot change order as there is no rules for LR or RL to change.
If the same, we check the relative i and j position and deal with it accordingly
"""
class Solution(object):
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        n = len(start)
        i, j = 0, 0
        while i < n and j < n:
            while i < n-1 and start[i] == 'X':
                i += 1
            while j < n-1 and end[j] == 'X':
                j += 1
            if start[i] != end[j]:
                return False
            if (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                return False
            i += 1
            j += 1
        return True
        
