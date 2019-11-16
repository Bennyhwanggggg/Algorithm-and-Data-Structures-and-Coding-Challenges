"""
Next Greater Element III

Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21
 

Example 2:

Input: 21
Output: -1

"""

"""
Time: O(N)
Space: O(N)

In this case as well, we consider the given number nn as a character array aa. First, we observe that for any given sequence that is in descending order, no next larger permutation is possible. For example, no next permutation is possible for the following array:

[9, 5, 4, 3, 1]

We need to find the first pair of two successive numbers a[i] and a[i−1], from the right, which satisfy a[i]>a[i−1]. Now, no rearrangements to the right of a[i−1] can create a larger permutation since that subarray consists of numbers in descending order. Thus, we need to rearrange the numbers to the right of a[i−1] including itself.

Now, what kind of rearrangement will produce the next larger number? We want to create the permutation just larger than the current one. Therefore, we need to replace the number a[i-1] with the number which is just larger than itself among the numbers lying to its right section, say a[j].

We swap the numbers a[i-1]and a[j]. We now have the correct number at index i-1. But still the current permutation isn't the permutation that we are looking for. We need the smallest permutation that can be formed by using the numbers only to the right of a[i−1]. Therefore, we need to place those numbers in ascending order to get their smallest permutation.
"""
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        s = list(map(int, str(n)))
        i = len(s)-1
        
        while i-1>=0 and s[i] <= s[i-1]:
            i -= 1
            
        if i==0:
            return -1
        
        j = i
        while j+1 < len(s) and s[j+1] > s[i-1]:
            j += 1
        
        s[i-1], s[j] = s[j], s[i-1]
        s[i:] = reversed(s[i:])
        ret = int(''.join(map(str, s)))
        
        return ret if ret<=((1<<31)-1) else -1

