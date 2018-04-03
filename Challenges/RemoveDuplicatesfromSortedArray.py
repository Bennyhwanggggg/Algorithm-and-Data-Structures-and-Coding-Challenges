class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # move duplicates to end of the array. Since we cannot modify the input array or use extra space we cannot use list(set(nums))

        if not nums:
            return 0

        tail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[tail]:
                tail += 1
                nums[tail] = nums[i]
        return tail + 1