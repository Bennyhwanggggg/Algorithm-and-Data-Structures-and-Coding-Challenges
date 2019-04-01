class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1
        return self.fib(N-1) + self.fib(N-2)

class Solution:
    memo = {}
    def fib(self, N: int) -> int:
        if(N == 1):
            self.memo[N] = 1
        elif(N == 0):
            self.memo[N] = 0
        elif(N in self.memo):
            return self.memo[N]
        else:
            self.memo[N] = self.fib(N-1) + self.fib(N-2)
    
        return self.memo[N]
