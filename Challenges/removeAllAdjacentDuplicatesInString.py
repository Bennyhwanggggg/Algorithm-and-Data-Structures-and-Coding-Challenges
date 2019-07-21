"""
Remove All Adjacent Duplicates In String

Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

 

Example 1:

Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""

"""
Algorithm

Initiate an empty output stack.

Iterate over all characters in the string.

Current element is equal to the last element in stack? Pop that last element out of stack.

Current element is not equal to the last element in stack? Add the current element into stack.

Convert stack into string and return it

Time: O(N)
Space: O(N-D) where D is the total length for all duplicates
"""
class Solution:
    def removeDuplicates(self, S: str) -> str:
        res = []
        for ch in S:
            if res and ch == res[-1]:
                res.pop()
            else:
                res.append(ch)
        
        return ''.join(res)
            

