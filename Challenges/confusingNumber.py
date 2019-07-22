"""
Confusing Number

Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

Example:
Input: 6
Output: true
Explanation: 
We get 9 after rotating 6, 9 is a valid number and 9!=6.

Example:
Input: 11
Output: false
Explanation: 
We get 11 after rotating 11, 11 is a valid number but the value remains the same, thus 11 is not a confusing number.
"""

class Solution:
    def confusingNumber(self, N: int) -> bool:
        invalid = {2, 3, 4, 5, 7}
        if N in invalid or N == 0:
            return False
        valid = {
            6: 9,
            9: 6,
            1: 1,
            8: 8,
            0: 0
        }
        
        curr = N
        new = ''
        while curr > 0:
            curr, temp = divmod(curr, 10)
            if temp in invalid:
                return False
            new += str(valid[temp])

        return int(new) != N
    
    def confusingNumber(N):
        x, y, cmap = N, 0, {0:0,1:1,6:9,8:8,9:6}
        while N:
            n, m = divmod(N, 10)
            if m not in cmap: return False
            N, y = n, y*10 + cmap[m]
        return x != y
    

class Solution:
    def confusingNumber(self, N):
        S = str(N)
        rotation = {"0" : "0", "1" : "1", "6" : "9", "8" : "8", "9" : "6"}
        result = []
        
        for c in S[::-1]:           # iterate in reverse
            if c not in rotation:
                return False
            result.append(rotation[c])
                
        return "".join(result) != S

