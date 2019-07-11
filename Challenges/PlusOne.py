"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        roundUp = False
        result = []
        for i in range(len(digits)-1, -1, -1):
            n = digits[i]
            if i == len(digits)-1:
                n += 1
            if roundUp:
                n += 1
                roundUp = False
            if n == 10:
                roundUp = True
                n = 0
            result.append(n)
        if roundUp:
            result.append(1)
        return result[::-1]
            

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]

        return [int(i) for i in str(num + 1)]
