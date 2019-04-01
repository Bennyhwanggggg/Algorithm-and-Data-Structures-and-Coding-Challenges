class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        count = 0
        seen = set()
        for n in A:
            if n in seen:
                return n
            seen.add(n)
