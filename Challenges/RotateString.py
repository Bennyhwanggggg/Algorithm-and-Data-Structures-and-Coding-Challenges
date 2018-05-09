class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if not A and B:
            return False
        max_rotate = len(A)
        count = 0
        while count <= max_rotate:
            if A == B:
                return True
            A = A[1:] + A[0]
            count += 1
        return False


class Solution2:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        for i in range(0, len(A) + 1):
            if A[i:] + A[0:i] == B:
                return True

        return False