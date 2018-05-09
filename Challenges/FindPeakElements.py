class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0

        for n in range(len(nums)):
            if not n:
                if nums[n] > nums[n + 1]:
                    return n
            elif n == len(nums) - 1:
                if nums[n] > nums[n - 1]:
                    return n
            elif nums[n] > nums[n - 1] and nums[n] > nums[n + 1]:
                return n
