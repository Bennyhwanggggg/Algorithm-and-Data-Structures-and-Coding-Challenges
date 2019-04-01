class Solution:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)):
        #   nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)
        
        swap = True
        for i in range(1, len(nums)):
          if swap:
            if nums[i-1] > nums[i]:
              nums[i-1], nums[i] = nums[i], nums[i-1]
          else:
            if nums[i-1] < nums[i]:
              nums[i-1], nums[i] = nums[i], nums[i-1]
          swap = not swap  
