"""
Number of Dice Rolls With Target Sum

You have d dice, and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways) modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000
"""

"""
Solution: DP
"""


"""
Solution: DFS with memo
"""
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        def helper(d, f, target):
            if (d, target) in dic:
                return dic[d, target]
            if target > f * d or target < d:
                return 0
            if target == 0 and d == 0:
                return 1
            res = 0
            for i in range(1, f+1):
                res += helper(d-1, f, target - i)
            dic[d, target] = res
            return res
        dic = {}
        return helper(d,f,target) % (10**9+7) # do this vecause the answer requires the modulo of this...
    
"""
Solution: DFS (time out)
"""
class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        nums = [n for n in range(1, f+1)]
        self.res = 0
        
        def backtracking(dice_remain, remain):
            if dice_remain == 0 and remain == 0:
                self.res += 1
                return
            
            if dice_remain > 0 and remain > 0:
                for n in nums:
                    backtracking(dice_remain-1, remain-n)
        
        backtracking(d, target)
        return self.res

