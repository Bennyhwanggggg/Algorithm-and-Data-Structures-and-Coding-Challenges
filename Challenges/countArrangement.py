class Solution:
    def countArrangement(self, N: int) -> int:
        """
            - Every number can be placed at the 1st position to satisfy condition 1
            - We just need to find a position in the rest that satisfy condition 2.
 
        """
        self.ret = 0
        candidates = set(range(1, N+1))
        self.backtrack(N, N, candidates)
        return self.ret
    
    def backtrack(self, N, index, candidates):
        if index == 1:
            self.ret += 1
        else:
            for i in candidates:
                if not i%index or not index%i:
                    self.backtrack(N, index-1, candidates-{i})
