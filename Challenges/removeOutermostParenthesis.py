"""
Remove Outermost Parenthese

A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:

Input: "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
Example 2:

Input: "(()())(())(()(()))"
Output: "()()()()(())"
Explanation: 
The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
Example 3:

Input: "()()"
Output: ""
Explanation: 
The input string is "()()", with primitive decomposition "()" + "()".
After removing outer parentheses of each part, this is "" + "" = "".
 

Note:

S.length <= 10000
S[i] is "(" or ")"
S is a valid parentheses string
"""

"""
Time: O(N)
Space: O(1)
"""
class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = ''
        count = 0
        
        for p in S:
            if p == '(':
                count += 1
                if count > 1:
                    res += p
            else:
                count -= 1
                if count > 0:
                    res += p
        return res


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        res = []
        count = 0
        for p in S:
            if p == '(':
                stack.append(p) # increment count of open parenthesis
                count += 1
            else:
                count -= 1 # decrement count of open parenthesis
                # we only append when there is more than one opening parenthesis
                # because we want to remove the outer most
                if len(stack) > 1:
                    stack.append(p)
                else:
                    stack.pop()
            if not count:
                if len(stack) > 2: # remove outer paranthesis
                    stack.pop(0)
                    stack.pop()
                res.extend(stack)
                stack = []
        if len(stack) > 2:
            stack.pop(0)
            stack.pop()
        res.extend(stack)
        return ''.join(res)
