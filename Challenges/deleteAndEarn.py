"""
Delete and Earn

Given an array nums of integers, you can perform operations on the array.

In each operation, you pick any nums[i] and delete it to earn nums[i] points. After, you must delete every element equal to nums[i] - 1 or nums[i] + 1.

You start with 0 points. Return the maximum number of points you can earn by applying such operations.

Example 1:

Input: nums = [3, 4, 2]
Output: 6
Explanation: 
Delete 4 to earn 4 points, consequently 3 is also deleted.
Then, delete 2 to earn 2 points. 6 total points are earned.
 

Example 2:

Input: nums = [2, 2, 3, 3, 3, 4]
Output: 9
Explanation: 
Delete 3 to earn 3 points, deleting both 2's and the 4.
Then, delete 3 again to earn 3 points, and 3 again to earn 3 points.
9 total points are earned.
"""

"""
DP

Intuition

Because all numbers are positive, if we "take" a number (use it to score points), we might as well take all copies of it, since we've already erased all its neighbors. We could keep a count of each number so we know how many points taking a number is worth total.

Now let's investigate what happens when we add a new number X (plus copies) that is larger than all previous numbers. Naively, our answer would be the previous answer, plus the value of X - which can be solved with dynamic programming. However, this fails if our previous answer had a number taken that was adjacent to X.

Luckily, we can remedy this. Let's say we knew using, the value of our previous answer, and avoid, the value of our previous answer that doesn't use the previously largest value prev. Then we could compute new values of using and avoid appropriately.

Algorithm

For each unique value k of nums in increasing order, let's maintain the correct values of avoid and using, which represent the answer if we don't take or take k respectively.

If the new value k is adjacent to the previously largest value prev, then the answer if we must take k is (the point value of k) + avoid, while the answer if we must not take k is max(avoid, using). Similarly, if k is not adjacent to prev, the answer if we must take k is (the point value of k) + max(avoid, using), and the answer if we must not take k is max(avoid, using).

At the end, the best answer may or may not use the largest value in nums, so we return max(avoid, using).


Time: O(N(log(N)))
Space: O(N)
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        prev = None
        avoid, using = 0, 0
        for k in sorted(counts):
            if k-1 != prev:
                avoid, using = max(avoid, using), k*counts[k]+max(avoid, using)
            else:
                avoid, using = max(avoid, using), k*counts[k] + avoid
            prev = k
        return max(avoid, using)

