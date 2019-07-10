"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""

"""
Time Complexity: O(N log N), where N is the length of A.

Space Complexity: O(N). 
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(x*x for x in A)
    
"""
Approach 2: Two Pointer
Intuition

Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing order, then some non-negative elements with squares in increasing order.

For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1], and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative part in reverse, and the positive part in the forward direction.

Algorithm

We can use two pointers to read the positive and negative parts of the array - one pointer j in the positive direction, and another i in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays together using a two-pointer technique.

Time Complexity: O(N), where N is the length of A.

Space Complexity: O(N). 
"""
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans

    
