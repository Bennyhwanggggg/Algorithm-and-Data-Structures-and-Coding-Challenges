"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

"""

"""
Time: O(n)
Space: O(1)

For each X from 1 to N, let's analyze whether X is good.

If X has a digit that does not have a valid rotation (3, 4, or 7), then it can't be good.

If X doesn't have a digit that rotates to a different digit (2, 5, 6, or 9), it can't be good because X will be the same after rotation.

Otherwise, X will successfully rotate to a valid different number.
"""
class Solution:
    def rotatedDigits(self, N: int) -> int:
        bad = {'3', '4', '7'}
        good = {'2', '5', '6', '9'}
        
        res = 0
        for n in map(str, range(1, N+1)):
            to_continue = True
            for k in bad:
                if k in n:
                    to_continue = False
                    break
            if to_continue:
                for k in good:
                    if k in n:
                        res += 1
                        break
        return res
        
        
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        counter = 0
        
        # digits that are valid after rotation
        valid_digits = set([0,1,2,5,6,8,9])
        # digits that are different after rotation
        flip_different = set([2,5,6,9])
        
        # iterate thru numbers
        for num in range(0,N+1):
            digits = [int(i) for i in str(num)]
            # to have a good number: 1) all digits have to be valid, 2) at least one digit is differnt after rotation
            if (set(digits).issubset(valid_digits) and set(digits).intersection(flip_different)):
                counter += 1
        
        return counter
