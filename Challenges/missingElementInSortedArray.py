"""
Missing Element in Sorted Array

Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

 

Example 1:

Input: A = [4,7,9,10], K = 1
Output: 5
Explanation: 
The first missing number is 5.
Example 2:

Input: A = [4,7,9,10], K = 3
Output: 8
Explanation: 
The missing numbers are [5,6,8,...], hence the third missing number is 8.
Example 3:

Input: A = [1,2,4], K = 3
Output: 6
Explanation: 
The missing numbers are [3,5,6,7,...], hence the third missing number is 6.
 

Note:

1 <= A.length <= 50000
1 <= A[i] <= 1e7
1 <= K <= 1e8
"""

"""
Binary search

judge miss element number between a and b by b-a-(idx_a-idx_b)
bi-search the index to find index i that satisfy missing number lie in nums[i] and nums[i+1].

Time: O(log(n))
Space: O(1)
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        
        while left < right:
            mid = (left+right+1)//2
            if nums[mid] - nums[0] - mid >= k:  # not the result index, result is in left part.
                right = mid - 1
            else:
                left = mid
        
        return nums[0] + left + k
