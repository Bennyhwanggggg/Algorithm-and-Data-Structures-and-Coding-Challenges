"""
Check If Word is Valid After Subsititutions

We are given that the string "abc" is valid.

From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated with Y) is equal to V.  (X or Y may be empty.)  Then, X + "abc" + Y is also valid.

If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc".  Examples of invalid strings are: "abccba", "ab", "cababc", "bac".

Return true if and only if the given string S is valid.

 

Example 1:

Input: "aabcbc"
Output: true
Explanation: 
We start with the valid string "abc".
Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".
Example 2:

Input: "abcabcababcc"
Output: true
Explanation: 
"abcabcabc" is valid after consecutive insertings of "abc".
Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".
Example 3:

Input: "abccba"
Output: false
Example 4:

Input: "cababc"
Output: false
 

Note:

1 <= S.length <= 20000
S[i] is 'a', 'b', or 'c'
"""

"""
Keep replacing
Time: O(N^2)
Space: O(1)
"""
class Solution:
    def isValid(self, S: str) -> bool:
        if len(S) < 3 or (len(S) == 3 and S != 'abc') or 'abc' not in S:
            return False
        
        while 'abc' in S:
            S = S.replace('abc', '')
        
        return not S


"""
Time: O(N)
Space: O(N)
"""
class Solution:
    def isValid(self, S: str) -> bool:
        
        N = len(S)
        if N % 3 or N == 0:
            return False
        
        arr = [None] * N
        arri = 0
        for c in S:
            arr[arri] = c
            arri += 1
            if arri >= 3 and arr[arri-3] == 'a' and arr[arri-2] == 'b' and arr[arri-1] == 'c':
                arri -= 3
        return arri == 0
