class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res = []

        def helper(lis):
            if len(lis) == len(nums):
                res.append(lis[:])
            else:
                for n in nums:
                    if n in lis:
                        continue
                    lis.append(n)
                    helper(lis)
                    lis.pop()

        helper([])
        return res