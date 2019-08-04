"""
Subarrays with K Different Integers

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

 

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
"""

"""
If there is some comment, it could be better. I take the liberty to add some:
This idea is to find the basic valid sub-array and find all its derived ones. If a valid sub-array A1 appears, code will push the right bound to reach its all derived sub-array (group) by checking the next number is in the dictionary or not; code will also cut number(s) from the left side, if the cutting does not change the validity, there is another group of sub-arrays (right_bound - current_index) exists.
The good point is that the right bound will not back trace, also does the left bound. So the time complexity is O(N).
"""
class Solution(object):
    def subarraysWithKDistinct(self, A, K):
        s = collections.Counter() 
        l = r = ans = 0 
        for i,num in enumerate(A):
            s[num] += 1
            if s[num] == 1 and len(s) == K:
                while r < len(A) and A[r] in s:
                    r += 1 
                while len(s) == K:
                    ans += r-i 
                    s[A[l]] -= 1 
                    if s[A[l]] == 0: 
			del s[A[l]] 
                    l += 1 
        return ans


"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        return self.atMostK(A, K) - self.atMostK(A, K - 1)

    def atMostK(self, A, K):
        res = ptr = 0
        counter = collections.Counter()
        for i, a in enumerate(A):
            counter[a] += 1
            while len(counter) > K:
                counter[A[ptr]] -= 1
                if not counter[A[ptr]]:
                    del counter[A[ptr]]
                ptr += 1    
            res += i - ptr + 1 
        return res  


class Solution:
    def subarraysWithKDistinct(self, A: 'List[int]', K: 'int') -> 'int':
        freq = {}
        start = 0
        start_k = 0
        res = 0
        for i, x in enumerate(A):
            freq[x] = freq.get(x, 0) + 1
            if len(freq) == K + 1:
                # remove the distinct at start_k, move start_k, start
                del freq[A[start_k]]
                start_k += 1
                start = start_k
            if len(freq) == K:
                # update start_k and res (Notice: K >= 1)
                while freq[A[start_k]] > 1:
                    freq[A[start_k]] -= 1
                    start_k += 1
                res += start_k - start + 1
        return res
