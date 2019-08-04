"""
Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

"""
O(N)
Let max or min result from A[0] to A[k] be MAX[k] or MIN[k]

The max result from A[0] to A[i] can only come from:
Decision 1. discard previous result, restart at A[i]
Decision 2. take A[i], MAX[i] = MAX[i-1] * A[i]
Decision 3. this is the most tricky part: A[i] can be negative, then MAX[i-1] * A[i] is negative (suppose MAX[i-1] is positive). Or a more complicated case: MIN[i-1] and MAX[i-1] are both negative, and A[i] is negative too, so that we need to take MIN[i-1] * A[i] into consideration.

Same thing to min result from A[0] to A[i].
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        r = nums[0]
        Max = [r] 
        Min = [r]
        
        for i, num in enumerate(nums[1:]): 
            if num >= 0:
                Max.append(max(num, Max[i] * num))
                Min.append(min(num, Min[i] * num))               
            else:
                Max.append(max(num, Min[i] * num))
                Min.append(min(num, Max[i] * num))        
        return max(Max)

