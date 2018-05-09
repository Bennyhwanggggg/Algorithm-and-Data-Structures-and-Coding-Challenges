class Solution:
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        teams = [str(i) for i in range(1, n+1)]
        last = len(teams)
        q = []
        while last > 1:
            left, right = 0, last - 1
            while left < right:
                q.insert(0, teams[left])
                q.insert(0, teams[right])
                left += 1
                right -= 1
            last //= 2
            i = 0
            while i < last:
                teams[i] = '({},{})'.format(q.pop(), q.pop())
                i += 1
        return teams[0]