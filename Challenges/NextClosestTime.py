


def nextClosestTime(time):
    h, m = time.split(":")
    curr = int(h) * 60 + int(m)
    for i in range(curr + 1, curr + 24 * 60 + 1):
        t = i % 1440
        h, m = t // 60, t % 60
        result = "{:02d}:{:02d}".format(h, m)
        if set(result) <= set(time):
            return result


"""
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
"""

"""
Solution 1: Simulation by converting to int and keep updating time till you get the next closest
Time: O(1) as we only try 24*60 possibilities
Space: O(1)
"""

"""
Solution 2: Build from allowed digits
Since we have 4 different digits, there are 4*4*4*4 possible combinations.
We check if each of them can be used on the clock and keep track of which one 
has the smallest difference from start time.
Time: O(1) since always 4*4*4*4 combinations
Space: O(1)
"""
class Solution(object):
    def nextClosestTime(self, time):
        ans = start = 60 * int(time[:2]) + int(time[3:])
        elapsed = 24 * 60
        allowed = {int(x) for x in time if x != ':'}
        for h1, h2, m1, m2 in itertools.product(allowed, repeat = 4):
            hours, mins = 10 * h1 + h2, 10 * m1 + m2
            if hours < 24 and mins < 60:
                cur = hours * 60 + mins
                cand_elapsed = (cur - start) % (24 * 60)
                if 0 < cand_elapsed < elapsed:
                    ans = cur
                    elapsed = cand_elapsed

        return "{:02d}:{:02d}".format(*divmod(ans, 60))
