class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        nums.sort()
        dp = [[]] * len(nums)
        dp[0] = [nums[0]]
        maxdp = dp[0]

        for i in range(1, len(nums)):
            dp[i] = [nums[i]]
            for j in range(i):
                if not nums[i] % dp[j][-1] and len(dp[i]) < len(dp[j]) + 1:
                    dp[i] = dp[j] + [nums[i]]
            if len(maxdp) < len(dp[i]):
                maxdp = dp[i]
        return maxdp

