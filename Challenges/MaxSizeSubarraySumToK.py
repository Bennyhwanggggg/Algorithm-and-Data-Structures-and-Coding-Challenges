class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        sum_table = {}  # key: sum(nums[:i+1]), value: i
        total = 0
        max_len = 0
        for i in range(len(nums)):
            total += nums[i]
            if total not in sum_table.keys():
                sum_table[total] = i
            remain = total - k
            if remain == 0:
                max_len = max(i + 1, max_len)
            elif remain in sum_table.keys():
                max_len = max(i - sum_table[remain], max_len)

        return max_len