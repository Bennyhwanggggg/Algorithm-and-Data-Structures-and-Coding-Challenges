class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1)*int(num2))


class Solution2:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        z = 0
        x = 0

        for i, element in enumerate(num1):
            for j in range(10):
                if element == a[j]:
                    z += j * (10 ** (len(num1) - i - 1))

        for c, b in enumerate(num2):
            for k in range(10):
                if b == a[k]:
                    x += k * (10 ** (len(num2) - c - 1))

        mul = z * x

        return (''.join('%d' % mul))