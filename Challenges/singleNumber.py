"""
Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        occurs = dict()
        for n in nums:
            if n not in occurs:
                occurs[n] = 1
            else:
                occurs[n] += 1

        for n in nums:
            if occurs[n] == 1:
                return n
        return -1

"""
If we take XOR of zero and some bit, it will return that bit
a⊕0=a
If we take XOR of two same bits, it will return 0
a⊕a=0

a⊕b⊕a=(a⊕a)⊕b=0⊕b=b

Time: O(N)
Space: O(1)
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = 0
        for n in nums:
            seen ^= n
        return seen
