"""
Single Number II

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""

"""
XOR operator can be used to detect the bit which appears odd number of times: 1, 3, 5, etc.
- XOR of zero and a bit results in that bit
- XOR of two equal bits (even if they are zeros) results in a zero
Using this, one could detect the bit which appears once, and the bit which appears three times. The problem is to distinguish between these two situations.

To separate number that appears once from a number that appears three times let's use two bitmasks instead of one: seen_once and seen_twice.

The idea is to
- change seen_once only if seen_twice is unchanged
- change seen_twice only if seen_once is unchanged

This way bitmask seen_once will keep only the number which appears once and not the numbers which appear three times.

Time: O(N)
Space: O(1)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)

        return seen_once

