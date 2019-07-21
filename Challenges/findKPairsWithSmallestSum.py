"""
Find K Pairs With Smallest Sums

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u,v) which consists of one element from the first array and one element from the second array.

Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]] 
Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [1,1],[1,1]
Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
Example 3:

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [1,3],[2,3]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""


"""
We know the brutal force way to do it is to calc (a1, b1), (a1, b2), (a1,b3)....(a3,b3)'s sum respectively and sort the sums, and pick the top 3 of them. This algorithm is O(n2). And we need an algorithm better than that.

So, the overall idea of the algorithm:
Maintain a min-heap to keep only part of the whole set of combinations of all elements from nums1 and nums2. That way, we can avoid the brutal force way which is O(n2). We only push necessary pairs into the heap, until we find all of the k pairs.

How we achieve that (for the sake of explanation, ignore the corner cases for now):
1, create a heap, then push (S0, N1, N2) into the heap, where N1 is the position of first element in nums1, N2 is the position of first element in nums2, S0 is the sum of N1 and N2. Mark (N1,N2) as visited.
2, Pop the root element (S0, N1,N2) out of the heap, add (N1,N2) to the result to be returned. and immediately push (S1, N1+1,N2) and (S2, N1, N2+1) into the heap, where S1 = nums1[N1+1]+nums2[N2], S2 = nums1[N1] + nums2[N2+1]. Here, if a pair (Nx, Ny) has already been visited, we'll ignore it and not push it to the heap.
3, repeat this, until all k pairs have been added into the return list. Return the list.

The complexity of this algorithm is O(klgk) if k<n, because we repeat k times, and each time we do a O(lgk) heappush.

Why this algorithm works? The real question is, in this algorithm, how do we know that the sum of the pair that got heappopped earlier is always smaller than the sum of any pair that got heappushed later. Why we so sure about that?

Because, look at the process:
We heappop the minimal pair (S0, N1, N2), then immediately heappush two larger pairs (S1, N1+1,N2) and (S2, N1, N2+1). (why S1 and S2 always larger than S0? Because the two arrays are sorted.) And right after the heappush, the heap gets re-heaped, and of course the root at this point is larger (at least equal) than (S0, N1, N2). Remember though, the root now maybe (S1, N1+1,N2) or (S2, N1, N2+1) or any other pair that already exists in the heap after that heappop operation. This process gets repeated over and over again until finished.

From this, we can conclude that, the pairs that get heappushed is always larger than the pairs that get heappopped earlier. It might be smaller than other pairs that are currently in the heap, but we don’t care about that. We only care about pairs that got pushed or popped.

The beauty of this algorithm is, it works perfectly under the fact: two array are sorted. If the arrays were to be unsorted, we would not be able to guarentee that the two pairs get heappushed are always larger than the pair that gets heappopped, thus it would be possible that a pair that gets heappopped later is larger than one gets heappopped ealier, which would fail to produce the correct answer.

Time: O(klog(k)) if k < n because we repeat k times and we do k times log(n) pushes fo heap
Space: O(n) n = number of pairs see visisted
"""
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        visited = set()
        heap = []
        output = []
        heapq.heappush(heap, (nums1[0]+nums2[0], 0, 0)) # sum, idx1, idx2
        visited.add((0, 0))

        while len(output) < k and heap:

            val = heapq.heappop(heap)
            idx1, idx2 = val[1:]
            output.append((nums1[idx1], nums2[idx2]))

            if idx1+1 < len(nums1) and (idx1+1, idx2) not in visited:
                heapq.heappush(heap, (nums1[idx1+1] + nums2[idx2], idx1+1, idx2))
                visited.add((idx1+1, idx2))

            if idx2+1 < len(nums2) and (idx1, idx2+1) not in visited:
                heapq.heappush(heap, (nums1[idx1] + nums2[idx2+1], idx1, idx2+1))
                visited.add((idx1, idx2+1))

        return output

