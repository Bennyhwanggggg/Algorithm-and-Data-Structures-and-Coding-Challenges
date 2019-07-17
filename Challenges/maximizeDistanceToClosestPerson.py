"""
Maximize distance to closeest person

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.

"""

"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        Using two pointers, consider three conditions

        starting value is 0 and the ending value is 1
        starting value is 1 and the ending value is 0
        starting value is 1 and the ending value is 1, there is at least one 1 between them
        """
        l, r, res, temp = 0, 0, 1, 0
        for i, v in enumerate(seats):
            if v == 0:
                r += 1
            elif v == 1:
                r = i
                if seats[l] == 0:  # if starts with zero
                    res = r - l
                else: 
                    temp = (r-l-1) // 2 if (r-l-1) % 2 == 0 else (r-l) // 2 # odd or even
                    
                    if temp > res:
                        res = temp
                l = i

        return res if res > r-l else r-l  # if starts with 1 and ends with zero

