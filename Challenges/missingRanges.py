"""
Missing Ranges

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
"""

"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        nums = [lower-1] + nums + [upper+1]
        ranges = []
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx-1] == 2:
                ranges.append(str(nums[idx]-1))
            elif nums[idx] - nums[idx-1] > 2:
                ranges.append(str(nums[idx-1]+1) + "->" + str(nums[idx]-1))
        return ranges

