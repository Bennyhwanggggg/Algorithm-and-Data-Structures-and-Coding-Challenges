class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        i = 0
        res = []

        while i < len(nums):
            n = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if nums[i] != n:
                res.append("{}->{}".format(n, nums[i]))
            else:
                res.append("{}".format(n))
            i += 1

        return res