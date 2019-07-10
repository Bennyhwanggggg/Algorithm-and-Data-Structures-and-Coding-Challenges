"""

Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result1 = 0
        result2 = 0

        for i in num1:
            result1 = result1*10 + (ord(i) - ord('0'))

        for i in num2:
            result2 = result2*10 + (ord(i) - ord('0'))
        s=''
        final_result = result1+result2
        string = ''
        while True:
            final_result, remainder = divmod(final_result, 10)
            string = chr(ord('0') + remainder) + string
            if final_result == 0:
                break
        return string

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) + int(num2))
