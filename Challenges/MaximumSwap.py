class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        digitsMap = {}
        for ind, n in enumerate(str(num)):
            digitsMap[n] = ind
        strCopy = list(str(num))
        for ind, n in enumerate(str(num)):
            for d in range(9, int(n), -1):
                digit = str(d)
                if digit in digitsMap and digitsMap[digit] > ind:
                    strCopy[ind], strCopy[digitsMap[digit]] = strCopy[digitsMap[digit]], strCopy[ind]
                    return int(''.join(strCopy))
        return num
