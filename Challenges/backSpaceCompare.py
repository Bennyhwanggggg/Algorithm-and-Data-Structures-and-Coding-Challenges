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


class Solution(object):
    def backspaceCompare(self, S, T):
        s = []
        t = []
        for c in S:
            if c == '#':
                if s != []:
                    s.pop()
            else:
                s.append(c)
        for c in T:
            if c == '#':
                if t != []:
                    t.pop()
            else:
                t.append(c)
        return s == t

class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return self.removeHashTags(S) == self.removeHashTags(T)
                
    def removeHashTags(self, s):
        skip = 0
        curr = ''
        for x in reversed(s):
            if x == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                curr += x
        return curr
        
   
                                    
