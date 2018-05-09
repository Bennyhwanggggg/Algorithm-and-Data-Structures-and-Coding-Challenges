class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return [[]]
        nums.sort()
        res = []

        def helper(lis, used):
            if len(lis) == len(nums):
                res.append(lis[:])
            else:
                preNum = nums[0] - 1
                for n in range(len(nums)):
                    if not used[n] and nums[n] != preNum:
                        preNum = nums[n]
                        lis.append(nums[n])
                        used[n] = True
                        helper(lis, used)
                        used[n] = False
                        lis.pop()

        helper([], [False] * len(nums))
        return res

class Solution2:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.permutation(nums, [],result)
        return result

    def permutation(self, numbers, curr, result):
        if len(numbers) == 0:
            result.append(curr)

        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            self.permutation(numbers[0:i]+numbers[i+1:], curr + [numbers[i]], result)