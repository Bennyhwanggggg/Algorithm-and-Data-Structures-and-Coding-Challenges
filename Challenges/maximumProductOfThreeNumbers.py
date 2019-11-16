"""
Maximum Product of Three Numbers

Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24
 

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
"""

"""
Linear scan using either product from smallest two (if two negative) * largest or 3 largest element
Time: O(N)
Space: O(1)
"""
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = float('inf'), float('inf')
        max1, max2, max3 = -float('inf'), -float('inf'), -float('inf')
        
        for n in nums:
            if n <= min1:
                min2 = min1
                min1 = n
            elif n <= min2:
                min2 = n
            
            if n >= max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n >= max2:
                max3 = max2
                max2 = n
            elif n >= max3:
                max3 = n
        
        return max(min1*min2*max1, max1*max2*max3)

