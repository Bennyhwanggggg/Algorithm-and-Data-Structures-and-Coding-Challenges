# class Solution:
#     def reversePairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        # naive solution
        # count = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] > 2*nums[j]:
        #             count += 1
        # return count


class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def helper(nums, start, end):
            if start >= end:
                return 0
            mid = (start + end) // 2
            res = helper(nums, start, mid) + helper(nums, mid + 1, end)
            nums[start:mid + 1] = sorted(nums[start:mid + 1])
            nums[mid + 1:end + 1] = sorted(nums[mid + 1:end + 1])
            i, j = start, mid + 1
            while i <= mid and j <= end:
                if nums[i] > 2 * nums[j]:
                    res += mid - i + 1
                    j += 1
                else:
                    i += 1

            return res

        return helper(nums, 0, len(nums) - 1)