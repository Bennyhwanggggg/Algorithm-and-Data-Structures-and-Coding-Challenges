class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = set([n for n in range(1, len(nums)+1)])
        for n in nums:
            if n in res:
                res.remove(n)
        return list(res)

    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [0] + nums
        for i in range(len(nums)):
            index = abs(nums[i])
            nums[index] = -abs(nums[index])

        return [i for i in range(len(nums)) if nums[i] > 0]