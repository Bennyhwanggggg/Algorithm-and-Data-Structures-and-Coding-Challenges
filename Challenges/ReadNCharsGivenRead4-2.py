# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):

    def __init__(self):
        self.queue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        num = 0

        while True:
            buf4 = [""] * 4
            size = read4(buf4)
            self.queue += buf4
            minSize = min(len(self.queue), n - num)
            if not minSize:
                break

            for i in range(minSize):
                buf[num] = self.queue.pop(0)
                num += 1

        return num