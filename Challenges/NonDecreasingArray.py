'''
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
'''
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        modified = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if modified: # terminate if second modification
                    return False
                # i>=2 to ensure we don't go out of bound
                if i >= 2 and nums[i] < nums[i-2]: # if current index is also less than the one after, move the modifed one ahead
                    nums[i] = nums[i-1]
                modified = True
        return True
        
