"""
Car Fleet

N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.


How many car fleets will arrive at the destination?

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Note:

0 <= N <= 10 ^ 4
0 < target <= 10 ^ 6
0 < speed[i] <= 10 ^ 6
0 <= position[i] < target
All initial positions are different.
"""

"""
Sort

Intuition

Call the "lead fleet" the fleet furthest in position.

If the car S (Second) behind the lead car F (First) would arrive earlier, then S forms a fleet with the lead car F. Otherwise, fleet F is final as no car can catch up to it - cars behind S would form fleets with S, never F.

Algorithm

A car is a (position, speed) which implies some arrival time (target - position) / speed. Sort the cars by position.

Now apply the above reasoning - if the lead fleet drives away, then count it and continue. Otherwise, merge the fleets and continue.


Sort the vehicles by the (pos, vel) pair.
Since the first vehicle will always lead a fleet, starting from the second vehicle, compare each vehicle's ideal arrival time with the arrival time of the fleet in front of it, i.e., stack[-1]. If its ideal arrival time is earlier, it will join the fleet in front of it. Otherwise, it will lead a new fleet and we append its arrival time into stack.
Finally, stack contains the arrival times of the fleets and the length of stack will be the number of distinct arrival times, i.e., the number of fleets.

Time: O(NlogN)
Space: O(N)
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, vel in sorted(zip(position, speed))[::-1]:
            dist = target - pos
            if not stack: # if first to arrive
                stack.append(dist / vel)
            elif dist / vel > stack[-1]: # if the current arrival time is after the lead
                stack.append(dist / vel)
        return len(stack)

