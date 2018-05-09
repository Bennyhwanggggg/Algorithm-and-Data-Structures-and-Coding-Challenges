class PhoneDirectory:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.numbers = [True for i in range(maxNumbers)]

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        nums = self.numbers
        for ind, avail in enumerate(nums):
            if avail:
                self.numbers[ind] = False
                return ind
        return -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return self.numbers[number]

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.numbers[number] = True

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)


class PhoneDirectory2:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.availabe = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.availabe.pop() if self.availabe else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.availabe

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.availabe.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)