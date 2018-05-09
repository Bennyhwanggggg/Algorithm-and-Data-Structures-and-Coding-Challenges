class Solution:
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = [0] * (target + 1)
        res[0] = 1
        for i in range(1, len(res)):
            for n in nums:
                if i - n >= 0:
                    res[i] += res[i - n]
        return res[target]


