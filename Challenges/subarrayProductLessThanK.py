class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not len(nums)or k<=1:
            return 0
        left, right = 0, 0
        res = 0
        prod = 1
        while right < len(nums):
            prod *= nums[right]
            right += 1
            while prod >=k:
                prod /= nums[left]
                left += 1
            res += right - left
        return res

class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        start, prod, cnt = 0, 1, 0
        for end in range(len(nums)):
            while start <= end and prod*nums[end] >= k:
                prod = prod/nums[start]
                start += 1
            prod = 1 if start > end else prod*nums[end]
            cnt = cnt if start > end else cnt+(end-start+1)
        return cnt
