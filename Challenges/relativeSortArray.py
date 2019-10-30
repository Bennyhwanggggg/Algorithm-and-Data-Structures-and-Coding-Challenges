"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""

"""
Time: O(N(log(N))
Space: O(N)
"""

def relativeSortArray(self, A, B):
        k = {b: i for i, b in enumerate(B)}
        return sorted(A, key=lambda a: k.get(a, 1000 + a))

"""
Time: O(N^2)
"""
class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in arr2:
            for j in arr1:
                if i == j:
                    res.append(j)
        
        unused = []
        for j in arr1:
            if j not in res:
                unused.append(j)
        
        unused.sort()
        res.extend(unused)
        return res
