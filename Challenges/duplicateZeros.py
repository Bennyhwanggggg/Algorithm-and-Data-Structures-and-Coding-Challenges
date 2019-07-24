"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
"""


# it requires us to do it in place, so we can't use extra space here
# we can do it in 2 passes, the first pass record the count of 0s as shifts
# the second pass put the shifted elements in the right spot and put 0s in the right spot
# e.g, [1,0,2,3,0,4,5,0] will be extended as [1,0,0,2,3,0,0,4],5,0,0, only the first 8 elememnts
# fit in the array
# TimeL O(n)
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        shift = 0
        l = len(arr)
        for i in range(l):
            if arr[i] == 0:
                shift += 1
        for i in range(l-1, -1, -1):
            # put the shifted number in the right spot
            if i + shift < l:
                arr[i+shift] = arr[i]
            # if we meet a 0, we need to duplicate 0
            if arr[i] == 0:
                shift -= 1
                if i + shift < l:
                    arr[i+shift] = 0

"""
Brute Force
Time: O(N^2)
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0 and i+1 < len(arr):
                temp = arr[i+1]
                arr[i+1] = 0
                for j in range(i+2, len(arr)):
                    temp2 = arr[j]
                    arr[j] = temp
                    temp = temp2
                i += 1
            i += 1

