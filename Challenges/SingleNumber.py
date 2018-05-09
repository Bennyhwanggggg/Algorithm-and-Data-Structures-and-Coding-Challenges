class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurs = dict()
        for n in nums:
            if n not in occurs:
                occurs[n] = 1
            else:
                occurs[n] += 1

        for n in nums:
            if occurs[n] == 1:
                return n
        return -1