class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        hashtable = dict()
        for i in A:
            for j in B:
                if -(i + j) not in hashtable:
                    hashtable[-(i + j)] = 0
                hashtable[-(i + j)] += 1

        count = 0
        for c in C:
            for d in D:
                if c + d in hashtable:
                    count += hashtable[c + d]
        return count