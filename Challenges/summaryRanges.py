"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
"""

"""
Intuition

A range covers consecutive elements. If two adjacent elements have difference larger than 11, the two elements does not belong to the same range.

Algorithm

To summarize the ranges, we need to know how to separate them. The array is sorted and without duplicates. In such array, two adjacent elements have difference either 1 or larger than 1. If the difference is 1, they should be put in the same range; otherwise, separate ranges.

We also need to know the start index of a range so that we can put it in the result list. Thus, we keep two indices, representing the two boundaries of current range. For each new element, we check if it extends the current range. If not, we put the current range into the list.

Don't forget to put the last range into the list. One can do this by either a special condition in the loop or putting the last range in to the list after the loop.

Time: O(n)
Space: O(1)
"""
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        res = []
        i = 0
        for j in range(len(nums)):
            if j + 1 < len(nums) and abs(nums[j+1] - nums[j]) == 1:
                continue
            if i == j:
                res.append(str(nums[i]))
            else:
                res.append('{}->{}'.format(nums[i], nums[j]))
            i = j + 1
                
        return res
        

class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        i = 0
        res = []

        while i < len(nums):
            n = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            if nums[i] != n:
                res.append("{}->{}".format(n, nums[i]))
            else:
                res.append("{}".format(n))
            i += 1

        return res
