class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        left, right, curr = 0, 0, 0
        minLen = len(nums) + 1
        while right < len(nums):
            curr += nums[right]
            while curr >= s:
                minLen = min(minLen, right - left + 1)
                curr -= nums[left]
                left += 1
            right += 1

        return minLen if minLen != (len(nums) + 1) else 0