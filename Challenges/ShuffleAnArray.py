class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.xlist = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.xlist

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        from random import shuffle
        from copy import deepcopy

        x = deepcopy(self.xlist)
        shuffle(x)
        return x

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()