"""
Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

"""
DP

Time and Space: O(N)

Find maximum height of bar from the left end upto an index i in the array left_max.
Find maximum height of bar from the right end upto an index i in the array right_max.
Iterate over the \text{height}height array and update ans:
Add min(max_left[i],max_right[i])−height[i] to ans
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        arr = []
        left, right = 0, 0
        water = 0
        
        for h in height:
            left = max(left, h)
            arr.append(left)
            
        for idx, h in enumerate(reversed(height)):
            right = max(right, h)
            water += min(arr[len(height)-1-idx], right) - h
        
        return water

class Solution:
    def trap(self, height: List[int]) -> int:
        
        res = 0
        arrLeft = []
        currLeft = 0
        
        for i in range(1, len(height)):
            currLeft = max(currLeft, height[i-1])
            arrLeft.append(currLeft)
        
        currRight = 0
        for i in range(len(height)-2, -1, -1):
            currRight = max(currRight, height[i+1])
            res += max(min(arrLeft[i], currRight) - height[i], 0)
        
        return res
        
