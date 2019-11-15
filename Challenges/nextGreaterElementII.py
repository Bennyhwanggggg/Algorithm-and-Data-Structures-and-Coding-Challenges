"""
Next Greater Element II

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

"""
Stack

Time and Space: O(N)

This approach makes use of a stack. This stack stores the indices of the appropriate elements from numsnums array. The top of the stack refers to the index of the Next Greater Element found so far. We store the indices instead of the elements since there could be duplicates in the nums array. The description of the method will make the above statement clearer.

We start traversing the numsnums array from right towards the left. For an element nums[i] encountered, we pop all the elements stack[top] from the stack such that stack[top] ≤ nums[i]. We continue the popping till we encounter a stack[top] satisfying stack[top] > nums[i]nums[stack[top]]>nums[i]. Now, it is obvious that the current stack[top] only can act as the Next Greater Element for nums[i](right now, considering only the elements lying to the right of nums[i]).

If no element remains on the top of the stack, it means no larger element than nums[i] exists to its right. Along with this, we also push the index of the element just encountered(nums[i]), i.e. ii over the top of the stack, so that nums[i](or stack[top]) now acts as the Next Greater Element for the elements lying to its left.

We go through two such passes over the complete nums array. This is done so as to complete a circular traversal over the numsnums array. The first pass could make some wrong entries in the resres array since it considers only the elements lying to the right of nums[i], without a circular traversal. But, these entries are corrected in the second pass.

"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1 for _ in range(len(nums))]
        
        stack = []
        for i in range(2*len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i%len(nums)]:
                stack.pop()
            
            res[i%len(nums)] = -1 if not stack else nums[stack[-1]]
            stack.append(i%len(nums))
        
        return res
