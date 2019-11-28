"""
Partition to K Equal Sum Subsets

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
 

Note:

1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
"""

"""
Backtracking, split into k buckets each with the target sum and use backtracking to fit numbers in

Time: O(2^N)
Space: O(2^N)???
"""
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        ASum = sum(nums)
        nums.sort(reverse=True)
        if ASum % k != 0:
            return False
        target = [ASum // k] * k

        def dfs(pos):
            if pos == len(nums): 
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos + 1):
                        return True
                    target[i] += nums[pos]
            return False
        return dfs(0)

