class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest = 0
        left, right = 0, len(height)-1
        while left < right:
            largest = max(largest, min(height[left], height[right]) * (right-left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return largest