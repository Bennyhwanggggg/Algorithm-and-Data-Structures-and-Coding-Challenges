class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return sorted([k for k, v in Counter(nums).most_common(k)])


class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        d = {}
        for n in nums:
            if n not in d:
                d[n] = 0
            d[n] += 1
        res = []
        count = 0
        for key in sorted(d, key=d.get, reverse=True):
            if count < k:
                res.append(key)
                count += 1
            else:
                break
        return res


class Solution3:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        hs, freq = {}, {}
        for n in nums:
            if n not in hs:
                hs[n] = 0
            hs[n] += 1

        for key, v in hs.items():
            if v not in freq:
                freq[v] = [key]
            else:
                freq[v].append(key)

        arr = []

        for x in range(len(nums), 0, -1):
            if x in freq:
                for i in freq[x]:
                    arr.append(i)

        return arr[:k]