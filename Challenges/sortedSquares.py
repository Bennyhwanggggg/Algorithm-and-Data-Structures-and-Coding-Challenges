class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for n in A:
            res.append(n**2)
        return sorted(res)
