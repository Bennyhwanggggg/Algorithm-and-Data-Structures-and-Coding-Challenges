"""
Combination Sum IV
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
 

Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""

"""
Explanation: Take the example in the question, where nums is [1, 2, 3] and the target is 4. Here's how you would build the solution bottom up by starting with the ways you can make a total of 1, then the number of ways you can make a total of 2, and so on up to 4:

1 -> [1]
2 -> [1, 1], [2]
3 -> [1, 1, 1], [1, 2], [2, 1]
4 -> [1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]

Since we just need the counts, not the actual combinations, this can be simplified to the following DP algorithm:

Pre-Step: Initialize the DP array to be 1 for each number in nums (since you can trivially make that total by just using that number itself) and 0 otherwise.
DP = [0, 1, 1, 1, 0]

Now for each number on the way to our target, call that sub-target t_sub. See how many ways we can make t_sub by taking each number n in nums and checking how many ways we were able to make t_sub - n then adding that to the DP entry for t_sub.

Step 1:
t_sub = 1
t_sub - 1 = 0 so add nothing
t_sub - 2 < 0 so add nothing
t_sub - 3 < 0 so add nothing
DP = [0, 1, 1, 1, 0]

Step 2:
t_sub = 2
t_sub - 1 = 1 so DP[2] += DP[1] and is now 2
t_sub - 2 = 0 so add nothing
t_sub - 3 < 0 so add nothing
DP = [0, 1, 2, 1, 0]

Step 3:
t_sub = 3
t_sub - 1 = 2 so DP[3] += DP[2] and is now 3
t_sub - 2 = 1 so DP[3] += DP[1] and is now 4
t_sub - 3 = 0 so add nothing
DP = [0, 1, 2, 4, 0]

Step 4:
t_sub = 4
t_sub - 1 = 3 so DP[4] += DP[3] and is now 4
t_sub - 2 = 2 so DP[4] += DP[2] and is now 6
t_sub - 3 = 1 so DP[4] += DP[1] and is now 7
DP = [0, 1, 2, 4, 7]

Now we are finished, so return DP[-1], which is the number of ways we can make t_sub when t_sub is the target.

Time: O(NT)
Space: O(T)
"""
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        dp = [0]*(target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
        return dp[target]
        


class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1, len(res)):
            for n in nums:
                if i - n >= 0:
                    res[i] += res[i - n]
        return res[target]


