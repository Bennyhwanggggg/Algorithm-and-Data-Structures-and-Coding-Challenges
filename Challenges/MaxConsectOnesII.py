class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre, curr, maxlen = -1, 0, 0
        for i in nums:
            if i == 0:
                pre, curr = curr, 0
            else:
                curr += 1
            maxlen = max(maxlen, pre + curr + 1)

        return maxlen