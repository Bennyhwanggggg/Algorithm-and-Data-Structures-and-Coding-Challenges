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
