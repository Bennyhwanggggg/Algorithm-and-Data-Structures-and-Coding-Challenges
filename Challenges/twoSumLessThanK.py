"""
Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S and S < K. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: A = [10,20,30], K = 15
Output: -1
Explanation: 
In this case it's not possible to get a pair sum less that 15.
 

Note:

1 <= A.length <= 100
1 <= A[i] <= 1000
1 <= K <= 2000
"""

"""
One pointer 
Time: O(n)
Space: O(1)
"""
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        
        i = len(A) - 1
        res = -float('inf')
        while i >= 0:
            if A[i] > K:
                i -= 1
            else:
                j = i-1
                while j >= 0 and A[i] + A[j] >= K:
                    j -= 1
                if j == -1:
                    i -= 1
                    continue
                res = max(res, A[i]+A[j])
                i -= 1
        
        return res if res != -float('inf') else -1
    
"""
Two pointer
Same time and space complexity
"""
def towSumLessThanK(A,K): 
		a = sorted(A) 
		i,j = 0,len(a)-1
        ans = -1
        while i<j:
            if a[i]+a[j]<K:
                ans = max(ans,a[i]+a[j])
                i += 1
            else:
                j -= 1
        return ans
