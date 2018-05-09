class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if len(timeSeries) == 1:
            return duration
        if not timeSeries:
            return 0

        total = 0
        for ind in range(1, len(timeSeries)):
            diff = timeSeries[ind] - timeSeries[ind - 1]
            if diff >= duration:
                total += duration
            else:
                total += diff

        total += duration
        return total