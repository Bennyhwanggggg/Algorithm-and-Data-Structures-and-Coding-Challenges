class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        evenMidCandidate = ["11", "69", "88", "96", "00"]
        oddMidCandidate = ["0", "1", "8"]
        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]
        if n % 2:
            pre, midCandid = self.findStrobogrammatic(n - 1), oddMidCandidate
        else:
            pre, midCandid = self.findStrobogrammatic(n - 2), evenMidCandidate

        mid = (n - 1) // 2
        return [p[:mid] + c + p[mid:] for c in midCandid for p in pre]
