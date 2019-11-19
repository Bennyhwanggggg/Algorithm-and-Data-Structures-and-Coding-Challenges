"""
Rearrange String k Distance Apart

Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.

All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.
"""


"""
Greedy, Always take the letter with highest count
Time: O(N)  Each heap operation takes constant time since it holds at most 26 elements. So this allows theta(n) time.
Space: O(N)
"""
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        counts = collections.Counter(s)
        heap = []
        for key in counts.keys():
            heapq.heappush(heap, (-counts[key], key))
        
        queue = collections.deque()
        res = []
        while heap:
            count, letter = heapq.heappop(heap)
            res.append(letter)
            count += 1
            queue.append((count, letter))
            if len(queue) < k:
                continue
            front = queue.popleft()
            if front[0] < 0:
                heapq.heappush(heap, front)
        return ''.join(res) if len(res) == len(s) else ''

