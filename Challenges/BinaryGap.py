class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        gap, maxGap = -1, 0
        while N>0:
            if gap >= 0:
                gap += 1
            if N%2 == 1:
                maxGap = max(maxGap, gap)
                gap = 0
            N //= 2
        return maxGap
        