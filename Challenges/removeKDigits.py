"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
"""


"""
Stack: Greedy
Time: O(N)
Space: O(N)
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for idx in range(len(num)):
            while stack and k > 0:
                if num[idx] < stack[-1]:
                    k -= 1
                    stack.pop()
                else:
                    break
            stack.append(num[idx])
        
        while k != 0:
            stack.pop()
            k -= 1
        
        while stack:
            if stack[0] == '0':
                stack = stack[1:]
            else:
                break
        
        return ''.join(stack) or '0'
    
"""
Another approach using heap similar to larget number subsequence with keeping track of index
"""

