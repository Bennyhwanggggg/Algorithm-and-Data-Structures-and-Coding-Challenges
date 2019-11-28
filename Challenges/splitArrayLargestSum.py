"""
Split Array Largest Sum

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

"""
Cumulative sum with memo backtracking
"""

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def helper(i, nums, m, cache, cums):
            if i == len(nums):
                return 0
            elif m == 1:
                return sum(nums[i:])
            else:
                if i in cache and m in cache[i]:
                    return cache[i][m]
                cache[i][m] = float('inf')
                for j in range(1,len(nums)+1):
                    left, right = cums[i+j] - cums[i], helper(i+j, nums, m-1, cache, cums)
                    cache[i][m] = min(cache[i][m], max(left, right))
                    if left > right:
                        break
                return cache[i][m]
    
        cums = [0]
        for x in nums:
            cums.append(cums[-1]+x)
        cache = collections.defaultdict(dict)            
        return helper(0, nums, m, cache, cums)
