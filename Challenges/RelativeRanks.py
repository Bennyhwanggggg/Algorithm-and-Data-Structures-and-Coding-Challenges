class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        cpy = sorted(nums)
        cpy.reverse()
        rank = [None for i in range(len(nums))]
        for r in range(len(nums)):
            ind = nums.index(cpy[r])
            if r == 0:
                rank[ind] = 'Gold Medal'
            elif r == 1:
                rank[ind] = 'Silver Medal'
            elif r == 2:
                rank[ind] = 'Bronze Medal'
            else:
                rank[ind] = str(r+1)
        return rank