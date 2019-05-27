"""
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Solution:
Note that every k-digit number can be broken into the leading 1 followed by (k-1)-digit numbers. Therefore, the number of 1's in the k-digit number is (1 + the number of 1's in the (k-1)-digit number).
Therefore, we start with record = [0,1], which is the solution for 1-digit binary numbers. The solution for 2-digit numbers is then appending record by (1+record), so on and so forth.
"""

class Solution:
    def countBits(self, num: int) -> List[int]:
        record = [0, 1]
        l = 2
        while l < num+1:
            record = record + [i+1 for i in record]
            l = l*2
        return record[0:num+1]
