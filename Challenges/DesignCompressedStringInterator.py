class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.ptr = 0
        self.ch = ' '
        self.rem = -1
        self.initialize()

    def initialize(self):
        if self.ptr == len(self.string):
            ch, rem = ' ', -1
        else:
            ch = self.string[self.ptr]
            self.ptr += 1
            rem = 0
            while self.ptr < len(self.string) and self.string[self.ptr].isdigit():
                rem = rem * 10 + int(self.string[self.ptr])
                self.ptr += 1
        self.ch, self.rem = ch, rem
        return

    def next(self):
        """
        :rtype: str
        """
        return_val = self.ch
        self.rem -= 1
        if not self.rem:
            self.initialize()
        return return_val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ch != ' '

# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()