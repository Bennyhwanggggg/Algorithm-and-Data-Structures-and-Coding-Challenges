"""
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

"""
Heap
Time complexity : O(Nlog(k)). The complexity of Counter method is O(N). To build a heap and output list takes O(Nlog(k)). Hence the overall complexity of the algorithm is O(N+Nlog(k))=O(Nlog(k)).

Space complexity : \mathcal{O}(N)O(N) to store the hash map.

The second step is to build a heap. The time complexity of adding an element in a heap is O(log(k)) and we do it N times that means O(Nlog(k)) time complexity for this step.

The last step to build an output list has O(klog(k)) time complexity.
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)  # This step takes O(N) time where N is number of elements in the list.
        return heapq.nlargest(k, count.keys(), key=count.get)


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
