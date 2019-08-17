"""
Maximum Swap

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.
Note:
The given number is in the range [0, 108]
"""

"""
Greedy
Time: O(N)
Space: O(1)
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(map(int, str(num)))
        last_occurrence = {n: idx for idx, n in enumerate(arr)}
        for idx, n in enumerate(arr):
            for d in range(9, n, -1):
                if last_occurrence.get(d, -float('inf')) > idx:
                    arr[idx], arr[last_occurrence[d]] = arr[last_occurrence[d]], arr[idx]
                    return int("".join(map(str, arr)))
        return num
    
"""
Another approach using heap similar to largestNumbersubsequence
"""


class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """

        digitsMap = {}
        for ind, n in enumerate(str(num)):
            digitsMap[n] = ind
        strCopy = list(str(num))
        for ind, n in enumerate(str(num)):
            for d in range(9, int(n), -1):
                digit = str(d)
                if digit in digitsMap and digitsMap[digit] > ind:
                    strCopy[ind], strCopy[digitsMap[digit]] = strCopy[digitsMap[digit]], strCopy[ind]
                    return int(''.join(strCopy))
        return num
