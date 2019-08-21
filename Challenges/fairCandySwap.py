"""
Fair Candy Swap

Alice and Bob have candy bars of different sizes: A[i] is the size of the i-th bar of candy that Alice has, and B[j] is the size of the j-th bar of candy that Bob has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the same total amount of candy.  (The total amount of candy a person has is the sum of the sizes of candy bars they have.)

Return an integer array ans where ans[0] is the size of the candy bar that Alice must exchange, and ans[1] is the size of the candy bar that Bob must exchange.

If there are multiple answers, you may return any one of them.  It is guaranteed an answer exists.

 

Example 1:

Input: A = [1,1], B = [2,2]
Output: [1,2]
Example 2:

Input: A = [1,2], B = [2,3]
Output: [1,2]
Example 3:

Input: A = [2], B = [1,3]
Output: [2,3]
Example 4:

Input: A = [1,2,5], B = [2,4]
Output: [5,4]
"""
"""
Intuition

If Alice swaps candy x, she expects some specific quantity of candy y back.

Algorithm

Say Alice and Bob have total candy S_A, S_B respectively.

If Alice gives candy xx, and receives candy y, then Bob receives candy x and gives candy y. Then, we must have

S_A - x + y = S_B - y + x
for a fair candy swap. This implies

y = x + (S_B - S_A)/2
 

Our strategy is simple. For every candy xx that Alice has, if Bob has candy y = x + (S_B - S_A)/2
 , we return [x, y]. We use a Set structure to check whether Bob has the desired candy yy in constant time.
Time Complexity: O(A.length+B.length).

Space Complexity: O(B.length)
"""
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sA, sB = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (sB-sA)//2 in setB:
                return [x, x + (sB-sA)//2]

