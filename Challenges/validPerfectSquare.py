"""
Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false
"""

"""
Binary Search
Time: O(log(N))
Space: O(1)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num < 2:
            return True
        left, right = 1, num//2
        while left <= right:
            x = (left+right) // 2
            guess = x*x
            if guess == num:
                return True
            if guess > num:
                right = x - 1
            else:
                left = x + 1
        return False

