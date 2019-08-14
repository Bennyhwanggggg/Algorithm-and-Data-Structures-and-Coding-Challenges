"""
Maximum of Absolute Value Expression

Given two arrays of integers with equal lengths, return the maximum value of:

|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|

where the maximum is taken over all 0 <= i, j < arr1.length.


Example 1:

Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
Output: 13
Example 2:

Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
Output: 20
 

Constraints:

2 <= arr1.length == arr2.length <= 40000
-10^6 <= arr1[i], arr2[i] <= 10^6
"""
"""
So, if we remove the abs, we find that there are four combinations:
(x_i+y_i+i) - (x_j+y_j+j); 
(x_i-y_i+i) - (x_j-y_j+j); 
(-x_i+y_i+i) - (-x_j+y_j+j); 
(-x_i-y_i+i) - (-x_j-y_j+j) ;
The reason I fix the sign of i and j is that we use the max of the list to minus the min of the list, thus shifting the sign of i doesn't matter.
And the result is the maximum of these four situations.
Thus we create the list as [x_i+y_i+i] and so on.

Time: O(N)
Space: O(N)
"""
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        l1, l2 ,l3, l4 = [], [], [], []
        for i in range(len(arr1)):
            l1 += [arr1[i]+arr2[i]+i]
            l2 += [arr1[i]-arr2[i]+i]
            l3 += [-arr1[i]+arr2[i]+i]
            l4 += [-arr1[i]-arr2[i]+i]
        res = []
        res += [max(l1)-min(l1)]
        res += [max(l2) -min(l2)]
        res += [max(l3)-min(l3)]
        res += [max(l4)-min(l4)]
        return max(res)

