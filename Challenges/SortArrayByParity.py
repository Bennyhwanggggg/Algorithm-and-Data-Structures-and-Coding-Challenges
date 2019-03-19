class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for n in A:
            if n%2:
                odd.append(n)
            else:
                even.append(n)
        even.extend(odd)
        return even