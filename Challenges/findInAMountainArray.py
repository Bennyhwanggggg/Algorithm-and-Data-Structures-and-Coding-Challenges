"""
Find in Mountain Array

(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10000
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
"""
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:
"""
Multiple Binary Searches
Time: O(nlog(n))
Space: O(1)
"""
class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        if mountain_arr.get(0) == target:
            return 0
        low, high = 0, mountain_arr.length()
        curr = (low + high) // 2
        while curr != low and curr != high:
            if mountain_arr.get(curr) > mountain_arr.get(curr-1) and mountain_arr.get(curr) > mountain_arr.get(curr+1):
                break
            elif mountain_arr.get(curr) > mountain_arr.get(curr-1):
                low = curr
            else:
                high = curr
            curr = (low + high) // 2
        
        mid = curr
        if mountain_arr.get(mid) == target:
            return mid
        
        low, high = 0, mid
        while low < high:
            mid = (low + high)//2
            mid_height = mountain_arr.get(mid)
            if mid_height == target:
                return mid
            elif mid_height < target:
                low = mid + 1
            else:
                high = mid
        
        low = mid
        high = mountain_arr.length()
        while low < high:
            mid = (low + high)//2
            mid_height = mountain_arr.get(mid)
            if mid_height == target:
                return mid
            elif mid_height > target:
                low = mid + 1
            else:
                high = mid
                
        return -1


