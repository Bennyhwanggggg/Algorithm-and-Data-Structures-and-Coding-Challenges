"""
Minimum Number of Arrows to Burst Balloons

There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

Example:

Input:
[[10,16], [2,8], [1,6], [7,12]]

Output:
2

Explanation:
One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
"""

"""
Greedy 

One could always track the end of the current balloon, and ignore all the balloons which end before it. Once the current balloon is ended (= the next balloon starts after the current balloon), one has to increase the number of arrows by one and start to track the end of the next balloon.

Sort the balloons by end coordinate x_end.

Initiate the end coordinate of a balloon which ends first : first_end = points[0][1].

Initiate number of arrows: arrows = 1.

Iterate over all balloons:

If the balloon starts after first_end:

Increase the number of arrows by one.

Set first_end to be equal to the end of the current balloon.

Return arrows.

Time: O(Nlog(N))
Space: O(1)
"""

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points.sort(key = lambda x:x[1])  # sort by end points
        
        count = 1
        end = points[0][1]
        for st, en in points:
            if end < st:  # if the current balloon starts after the end of another one,
                # one needs one more arrow
                count += 1
                end = en
        
        return count

