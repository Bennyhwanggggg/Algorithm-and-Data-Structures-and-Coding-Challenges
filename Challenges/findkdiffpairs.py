class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) < 2:
            return 0
        nums.sort()
        count = 0
        i, j = 0, 1
        while j < len(nums):
            j = max(i + 1, j)
            while j < len(nums) and abs(nums[j] - nums[i]) < k:
                j += 1
            if j < len(nums) and abs(nums[j] - nums[i]) == k:
                count += 1
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1
        return count

