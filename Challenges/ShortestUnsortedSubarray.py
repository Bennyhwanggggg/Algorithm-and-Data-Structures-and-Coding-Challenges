class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sortednums = sorted(nums)
        start = 0
        for i in range(len(nums)):
            if nums[i] != sortednums[i]:
                start = i
                break

        end = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != sortednums[i]:
                end = i
                break
        if not end and not start:
            return 0
        return end - start + 1
