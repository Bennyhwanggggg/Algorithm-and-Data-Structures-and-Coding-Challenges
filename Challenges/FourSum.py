class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rtype = []
        
        avail = set()
        nums.sort()
        
        if len(nums)<4:
            return rtype
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k = j+1
                l = len(nums)-1;
                
                while k<l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    elif sum==target:
                        result = [nums[i], nums[j], nums[k], nums[l]]
                        if tuple(result) not in avail:
                            rtype.append(result)
                            avail.add(tuple(result))
                        k += 1
                        l -= 1
                            
        return rtype