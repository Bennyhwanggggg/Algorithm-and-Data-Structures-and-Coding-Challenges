class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sorted_nums = sorted(nums)
        for i in list(range(1, len(nums), 2)) + list(range(0, len(nums), 2)) :
            nums[i] = sorted_nums.pop()
