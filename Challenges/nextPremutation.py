"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.
"""

"""
Time: O(n), worse case two scan of the array, but sort is nlog(n), better apprace is to use swap at the end since we already know it is in ascending order when we scan from right to left.
Space: O(1)
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums)-2
        
        # find the first decreasing element
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
            
        # while scaning from right to left, we know it is in increasing order
        # so we swap the number just larger than the decreasing element with the decreasing 
        # element, then reverse the order of everything from the decreasing element
        if i>= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            
            nums[i], nums[j] = nums[j], nums[i]
            
        # place those number in ascending order
        nums[i+1:] = sorted(nums[i+1:])
            
        
        

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        pointer = len(nums)-2
        while pointer >= 0:
            if nums[pointer] < nums[pointer+1]:
                break
            pointer -= 1
        if pointer < 0:
            nums.sort()
            return
        pointer2 = pointer + 1
        while pointer2 < len(nums) and nums[pointer] < nums[pointer2]:
            pointer2 += 1
        nums[pointer2-1], nums[pointer] = nums[pointer], nums[pointer2-1]
        nums[pointer+1:] = sorted(nums[pointer+1:])
