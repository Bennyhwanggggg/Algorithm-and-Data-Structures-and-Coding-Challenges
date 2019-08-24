"""
WildCard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

"""
Recusion with memo

Intuition

Clean up the input by replacing more than one star in a row by a single star: p = remove_duplicate_stars(p).

The first idea here is a recursion. That's a straightforward approach but quite time consuming because of huge recursion depth for long input strings.

If the strings are equal p == s, return True.

If the pattern matches whatever string p == '*', return True.

If p is empty, or s is empty, return False.

If the current characters match p[0] == s[0] or p[0] == '?', then compare the next ones and return isMatch(s[1:], p[1:]).

If the current pattern character is a star p[0] == '*', then there are two possible situations:

The star matches no characters, and hence the answer is isMatch(s, p[1:]).

The star matches one or more characters, and so the answer is isMatch(s[1:], p).

If p[0] != s[0], return False.

Time: O(2^n)
Space: O(2^n)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        self.cache = dict()
        
        def backtracking(s, p):
            if (s, p) in self.cache:
                return self.cache[(s, p)]
            if p == s or p == '*':
                self.cache[(s, p)] = True
            elif len(p) == 0 or len(s) == 0:
                self.cache[(s, p)] = False
            elif p[0] == s[0] or p[0] == '?':
                self.cache[(s, p)] = backtracking(s[1:], p[1:])
            elif p[0] == '*':
                self.cache[(s, p)] = backtracking(s, p[1:]) or backtracking(s[1:], p) 
            else:
                self.cache[(s, p)] = False
            return self.cache[(s, p)]
        
        p = self.remove_duplicate_stars(p)
        return backtracking(s, p)
        
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1) 
    
"""
DP
Time: O(SP)
Space: O(SP)
"""
class Solution:
    def isMatch(self, s, p):
        s_len = len(s)
        p_len = len(p)
        
        # base cases
        if p == s or p == '*':
            return True
        if p == '' or s == '':
            return False
        
        # init all matrix except [0][0] element as False
        d = [ [False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True
        
        # DP compute 
        for p_idx in range(1, p_len + 1):
            # the current character in the pattern is '*'
            if p[p_idx - 1] == '*':
                s_idx = 1
                # d[p_idx - 1][s_idx - 1] is a string-pattern match 
                # on the previous step, i.e. one character before.
                # Find the first idx in string with the previous math.
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                # If (string) matches (pattern), 
                # when (string) matches (pattern)* as well
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                # If (string) matches (pattern), 
                # when (string)(whatever_characters) matches (pattern)* as well
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            # the current character in the pattern is '?'
            elif p[p_idx - 1] == '?':
                for s_idx in range(1, s_len + 1): 
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1] 
            # the current character in the pattern is not '*' or '?'
            else:
                for s_idx in range(1, s_len + 1): 
                    # Match is possible if there is a previous match
                    # and current characters are the same
                    d[p_idx][s_idx] = \
                    d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]  
                                                               
        return d[p_len][s_len]
                     

