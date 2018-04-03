class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = {}
        res = []
        for n in nums1:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for i in nums2:
            if i in d and d[i]:
                res.append(i)
                d[i] -= 1

        return res