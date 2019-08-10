"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.


Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

"""
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = []
        odd, even = [], []
        for n in A:
            if n%2:
                odd.append(n)
            else:
                even.append(n)
        
        for o, e in zip(odd, even):
            res.append(e)
            res.append(o)
        return res

"""
In place
First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too. So let's only focus on A[0], A[2], A[4], ...

Ideally, we would like to have some partition where everything to the left is already correct, and everything to the right is undecided.

Indeed, this idea works if we separate it into two slices even = A[0], A[2], A[4], ... and odd = A[1], A[3], A[5], .... Our invariant will be that everything less than i in the even slice is correct, and everything less than j in the odd slice is correct.

Algorithm

For each even i, let's make A[i] even. To do it, we will draft an element from the odd slice. We pass j through the odd slice until we find an even element, then swap. Our invariant is maintained, so the algorithm is correct.

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


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
