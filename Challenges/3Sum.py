class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        res = set()
        nums.sort()
        for i, val in enumerate(nums[:-2]):
            # get rid of duplicates
	    if i >= 1 and val == nums[i-1]:
                continue
            d = set()
            for x in nums[i+1:]:
                n = -val-x
                if x not in d:
                    d.add(n)
                else:
                    res.add((val, n, x))
        return [list(sol) for sol in res]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = set()
        nums.sort()
        for ind, val in enumerate(nums[:-2]):
            seen = set()
            for x in nums[ind+1:]:
                n = -val-x
                if x not in seen:
                    seen.add(n)
                else:
                    result.add((val, x, n))
        return [list(sol) for sol in result]
