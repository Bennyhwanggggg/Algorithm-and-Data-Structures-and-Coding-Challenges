"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

"""
Two scan binary search to find each end
Time: O(log n)
spcae: O(1)
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not len(nums):
            return [-1, -1]
        low, high = 0, len(nums)-1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        
        if nums[low] != target:
            return [-1, -1]

        res = [low]
        high = len(nums) - 1
        
        while low < high:
            mid = ((low + high) // 2) + 1
            if nums[mid] >
            target:
                high = mid-1
            else:
                low = mid
        res.append(high)
        return res
        
"""
The search helper function returns an index range just like the requested searchRange function, but only searches in nums[lo..hi]. It first compares the end points and immediately returns [lo, hi] if that whole part of nums is full of target, and immediately returns [-1, -1] if target is outside the range. The interesting case is when target can be in the range but doesn't fill it completely.

In that case, we split the range in left and right half, solve them recursively, and combine their results appropriately. Why doesn't this explode exponentially? Well, let's call the numbers in the left half A, ..., B and the numbers in the right half C, ..., D. Now if one of them immediately return their [lo, hi] or [-1, -1], then this doesn't explode. And if neither immediately returns, that means we have A <= target <= B and C <= target <= D. And since nums is sorted, we actually have target <= B <= C <= target, so B = C = target. The left half thus ends with target and the right half starts with it. I highlight that because it's important. Now consider what happens further. The left half gets halved again. Call the middle elements a and b, so the left half is A, ..., a, b, ..., B. Then a <= target and:

If a < target, then the call analyzing A, ..., a immediately returns [-1, -1] and we only look further into b, ..., B which is again a part that ends with target.
If a == target, then a = b = ... = B = target and thus the call analyzing b, ..., B immediately returns its [lo, hi] and we only look further into A, ..., a which is again a part that ends with target.
Same for the right half C, ..., D. So in the beginning of the search, as long as target is only in at most one of the two halves (so the other immediately stops), we have a single path. And if we ever come across the case where target is in both halves, then we split into two paths, but then each of those remains a single path. And both paths are only O(log n) long, so we have overall runtime O(log n).
"""                
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not len(nums):
            return [-1, -1]
        
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) / 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        
        return search(0, len(nums)-1)
