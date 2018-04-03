class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if num is None or len(num) < 3:
            return False
        n = len(num)
        for i in range(1, n//2):
            if i > 1 and num[0] == '0':
                break
            for j in range(i+1, ((i+n)//2)+1):
                first, second, third = 0, i, j
                if num[second] == '0' and third > second + 1:
                    break
                while third < n:
                    result = str(int(num[first:second]) + int(num[second:third]))
                    if num[third:].startswith(result):
                        first, second, third = second, third, third + len(result)
                    else:
                        break
                if third == n:
                    return True
        return False