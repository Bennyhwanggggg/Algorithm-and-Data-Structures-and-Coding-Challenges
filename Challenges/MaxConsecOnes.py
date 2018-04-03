class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX = 0
        count = 0
        for i in nums:
            if i:
                count += 1
                if count > MAX:
                    MAX = count
            else:
                count = 0

        return MAX
