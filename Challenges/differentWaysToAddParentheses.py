"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""


"""
Find combinations using divide and conquer

(base) case 1: if there is 0 symbol, 
	we simply add input to result list;
case 2: if there is 1 symbol, 
	e.g., 1 s 2, we calculate the input and the result add to result list;
case 3: if there are 2 symbols, 
	e.g., 1 s 2 s 3, we can add parentheses when we meet a symbol as below:
	1 s (2 s 3) and (1 s 2) s 3.
	In this way, 1, (2 s 3), (1 s 2), and 3 can all be solved based on the above base cases, and we combine the result accoringly and add to result list.
    
    
...
for case n, we separate the expression into 2 parts at each position of symbol, 
and solve the two parts separately following the same pattern, and combine them accordingly.

The time complexity is O(2^n) exponential, for n is the number of operators in the input. That's because each function call calls itself twice unless it has been recursed n times.

The gist of this one is that we need to find all possible groupings of expressions and combine them - a classic case of "base case and build." We split up our string by operators, recursively take the possible results from the left side, recursively take the possible results from the right side, and combine them using the operator in the middle of the string. If there are no operators in the string, we know that the string must be a number - this is our base case. Continue to combine the results until we get back to the root of our recursion tree, and this is our final result. Using memoization prunes a lot of the recursion tree and saves a lot of time and memory when compared to the non-memoized version.
"""
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res
        
    def helper(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        return a*b
    
"""
Optimisation with memo
O(n) where n is number of sub problem which is each operator
"""
class Solution:
    def diffWaysToCompute(self, input: str, memo={}) -> List[int]:
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in '-+*':
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res
        
    def helper(self, a, b, op):
        if op == '+':
            return a+b
        elif op == '-':
            return a-b
        return a*b

