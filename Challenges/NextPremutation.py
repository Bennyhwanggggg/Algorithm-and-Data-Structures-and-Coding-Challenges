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