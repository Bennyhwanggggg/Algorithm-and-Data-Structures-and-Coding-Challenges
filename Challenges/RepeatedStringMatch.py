class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """

        temp = ""
        count = 0
        while (len(temp) < len(B)):
            temp += A
            count += 1
            if B in temp:
                return count
        temp += A
        if B in temp:
            return count + 1
        else:
            return -1

