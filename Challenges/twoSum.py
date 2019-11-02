class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] in seen:
                return [seen[nums[i]], i]
            else:
                seen[diff] = i
