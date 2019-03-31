class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for n in A:
            if n%2:
                odd.append(n)
            else:
                even.append(n)
        result = []
        for i in range(len(A)):
            if i%2:
                result.append(odd.pop())
            else:
                result.append(even.pop())
        return result
