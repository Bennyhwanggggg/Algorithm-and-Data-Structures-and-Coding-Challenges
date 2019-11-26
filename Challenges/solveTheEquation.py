"""
Solve the Equation


Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

If there is no solution for the equation, return "No solution".

If there are infinite solutions for the equation, return "Infinite solutions".

If there is exactly one solution for the equation, we ensure that the value of x is an integer.

Example 1:
Input: "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:
Input: "x=x"
Output: "Infinite solutions"
Example 3:
Input: "2x=x"
Output: "x=0"
Example 4:
Input: "2x+3x-6x=x+2"
Output: "x=-1"
Example 5:
Input: "x=x+2"
Output: "No solution"
"""

"""
Time, Space : O(N)
"""
class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def oneSide(s):
            sign, n = 1, len(s)
            # i, coef, const stand for current index, and accumulative 'x' coefficient and constant
            i = coef = const = 0
            while i < n:
                if s[i] == '+':
                    sign = 1
                elif s[i] == '-':
                    sign = -1
                elif s[i].isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    tmp = int(s[i:j])
                    if j < n and s[j] == 'x':
                        coef += tmp * sign
                        j += 1
                    else:
                        const += tmp * sign
                    i = j-1
                else:
                    coef += 1 * sign
                i += 1
            return coef, const
        
        left, right = equation.split('=')
        k1, b1 = oneSide(left)
        k2, b2 = oneSide(right)
        
        ans = 'x=' + str((b2 - b1) // (k1 - k2)) if k1 != k2 and b1 != b2 \
              else "Infinite solutions" if k1 == k2 and b1 == b2 \
              else "No solution" if b2 != b1 else 'x=0'
        return ans
            
        

