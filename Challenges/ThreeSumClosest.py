class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = float('inf')
        for i in range(len(nums)-2):
            # do binary search on rest of the list
            left, right = i+1, len(nums)-1
            while left < right:
                sumOfThree = nums[i] + nums[left] + nums[right]
                if abs(sumOfThree - target) < abs(res - target):
                    res = sumOfThree
                if sumOfThree > target:
                    right -= 1
                elif sumOfThree < target:
                    left += 1
                else:
                    return sumOfThree
        return res
            