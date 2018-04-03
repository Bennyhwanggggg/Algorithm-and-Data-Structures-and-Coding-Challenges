# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        num = 0
        buf4 = [None] * 4

        while True:
            size = read4(buf4)
            minSize = min(size, n - num)
            if not minSize:
                break

            for i in range(minSize):
                buf[num] = buf4[i]
                num += 1

        return num
