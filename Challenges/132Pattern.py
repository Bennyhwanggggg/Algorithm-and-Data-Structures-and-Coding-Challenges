"""
132 Pattern

Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""

"""
Stack: Time and Space O(N)

The preprocessing required is to just find the best nums[i] value corresponding to every nums[j] value. This is done in the same manner as in the second approach i.e. we find the minimum element found till the jth element which acts as the nums[i] for the current nums[j]. We maintain thes values in a minmin array. Thus, min[j] now refers to the best nums[i] value for a particular nums[j].

Use stack from right to left. Get rid of all elements in stack that are less than the current index's min as they will not meet the criteria. If top of stack has a number that is less than current num, we have a solution since the stack consists of elements on the right of current index.

"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minNums = [num for num in nums]
        
        minNum = nums[0]
        for idx, num in enumerate(minNums):
            minNum = min(minNum, num)
            minNums[idx] = minNum
        
        stack = []
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > minNums[j]:
                while stack and stack[-1] <= minNums[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False

