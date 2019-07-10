"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        return self.addBackspace(S) == self.addBackspace(T)
        
    def addBackspace(self, text):
        for i in range(len(text)):
            if text[i] == '#':
                text[i] = ''
                current = i-1
                while current > 0 and text[current] == '':
                    current -= 1
                if current >= 0:
                    text[current] = ''
        return ''.join(text)
                
