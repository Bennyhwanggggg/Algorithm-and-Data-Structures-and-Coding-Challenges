"""
4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

"""
Use two two sums
Time: O(n^2) to construct nums_dict
2nd part:
consider the worst case, say the input list is [0, 0, 0, ......0], the lengths of list1 and list2 are both n(n-1)/2, then the time complexity of the second part is n*(n(n-1)/2)^2
consider the best case, the lengths of list1 and list2 are both 1, then the time complexity of the 2nd part is n.

Space: O(n^2)
"""
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        results = set()
        nums_dict = collections.defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                total = nums[i] + nums[j]
                nums_dict[total].append((i, j))
        
        for val in nums_dict:
            diff = target - val
            if diff in nums_dict:
                list1 = nums_dict[val]
                list2 = nums_dict[diff]
                for (i, j) in list1:
                    for (k, l) in list2: 
                        if i != k and i != l and j!= k and j != l: # dont need number in same position
                            result = [nums[i], nums[j], nums[k], nums[l]]
                            result.sort()
                            results.add(tuple(result))
        
        return [list(res) for res in results]
                
            
        

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
