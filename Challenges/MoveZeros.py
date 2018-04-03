class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = 0
        for n in nums:
            if n != 0:
                count += 1

        count2 = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count2] = nums[i]
                count2 += 1

        for i in range(count, len(nums)):
            nums[i] = 0
