class Solution:
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        res = {x : i for i, x in enumerate(B)}
        return [res[n] for n in A]